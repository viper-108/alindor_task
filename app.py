import os
from flask import Flask, render_template, request, redirect, url_for, jsonify
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired
from werkzeug.utils import secure_filename
from deepgram import Deepgram
import openai

app = Flask(__name__)
# app.secret_key = os.environ.get('FLASK_SECRET_KEY')
app.secret_key = 'f99719a8da8e3bffeed7cc873786c343'
app.config['UPLOAD_FOLDER'] = 'uploads/'

os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
openai.api_key = os.getenv("OPENAI_API_KEY")
DEEPGRAM_API_KEY = os.getenv("DEEPGRAM_API_KEY")

class UploadForm(FlaskForm):
    audio = FileField(validators=[FileRequired()])

@app.route('/', methods=['GET', 'POST'])
def upload():
    form = UploadForm()
    if form.validate_on_submit():
        audio_file = form.audio.data
        filename = secure_filename(audio_file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        audio_file.save(filepath)

        # Process the audio file for sentiment analysis
        transcript = transcribe_audio(filepath)
        sentiment = analyze_sentiment_with_openai(transcript)
        
        return jsonify({
            "transcript": transcript,
            "sentiment": sentiment
        })
    return render_template('upload.html', form=form)

async def transcribe_audio(file_path):
    """Transcribe the given audio file using Deepgram."""
    dg_client = Deepgram(DEEPGRAM_API_KEY)
    with open(file_path, 'rb') as audio:
        source = {'buffer': audio, 'mimetype': 'audio/wav'}
        response = await dg_client.transcription.prerecorded(source, {'punctuate': True})
        transcript = response['results']['channels'][0]['alternatives'][0]['transcript']
    return transcript

def analyze_sentiment_with_openai(text):
    """Analyze sentiment using OpenAI's API."""
    response = openai.Completion.create(
      engine="text-davinci-003",
      prompt=f"What is the sentiment of this text? \"{text}\"",
      temperature=0,
      max_tokens=60,
      top_p=1.0,
      frequency_penalty=0.0,
      presence_penalty=0.0
    )
    return response.choices[0].text.strip()

if __name__ == '__main__':
    app.run(debug=True)

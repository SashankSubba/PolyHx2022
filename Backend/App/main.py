from db import db_connect, auth_user, get_emergency_contacts, post_encounter
from flask import Flask, request, redirect, url_for, flash, session, make_response
from flask_cors import CORS
from twilio.rest import Client

import json
import os.path
import requests
import time
import yaml
import os

RECORDING_FOLDER = '/recordings'
ALLOWED_EXTENSIONS = {'mp3'}

app = Flask(__name__)
CORS(app, resources={r"*": {"origins": "*"}})
uploads_dir = "uploads"

API_KEY = ''
TWILIO_API_KEY = ''
TWILIO_AUTH_TOKEN = ''
config_path = os.path.join(app.root_path, 'config.yml')
print(config_path)

with open(config_path, "r") as yamlfile:
    data = yaml.load(yamlfile, Loader=yaml.FullLoader)
    print("Read successful")
    print(data["ASSEMBLYAI_API_KEY"])
    API_KEY = data["ASSEMBLYAI_API_KEY"]
    TWILIO_API_KEY = data["TWILIO_API_KEY"]
    TWILIO_AUTH_TOKEN = data["TWILIO_AUTH_TOKEN"]


@app.route("/")
def index():
    return "<p>Hello, Test succeeded!</p>"


@app.route('/login', methods=['GET', 'POST'])
def login():
    conn = db_connect()
    error = None

    if request.method == 'POST':
        data = json.loads(request.data)
        email = data['email']
        password = data['password']
        user_obj = auth_user(conn, email, password)

        if user_obj["firstName"] is None:
            error = 'Incorrect Login'

        if error is None:
            # session.clear()
            # session['user_id'] = user['id']
            redirect(url_for('index'))
            return user_obj
        else:
            return error

    return make_response(200)

    # return "<p>Hello, World!</p>"


@app.route("/recording", methods=['POST'])
def post_audio():
    # check if the post request has the file part
    file = request.files['file']

    if file.filename == '':
        return 'No selected file'

    if file and allowed_file(file.filename):
        file_path = os.path.join(uploads_dir, file.filename)
        file.save(file_path)

        headers = {'authorization': API_KEY}
        response = requests.post('https://api.assemblyai.com/v2/upload', headers=headers, data=read_file(file_path))
        json = response.json()
        audio_url = json['upload_url']

        json = {
            "audio_url": audio_url,
            "sentiment_analysis": "true"
        }

        headers = {
            "authorization": API_KEY,
            "content-type": "application/json"
        }

        response = requests.post("https://api.assemblyai.com/v2/transcript", json=json, headers=headers)
        json = response.json()

        transcription_id = json['id']

        postAudio(transcription_id)

        status = checkAudioStatus(transcription_id)

        while status != "completed":
            app.logger.info("request is not completed yet")
            time.sleep(5)
            status = checkAudioStatus(transcription_id)
            if status == "error":
                app.logger.info("request failed")
                return "Error processing transcription"

        if status == "completed":
            getTranscriptionResult(transcription_id)

        return transcription_id


@app.route('/encounter', methods=['POST'])
def create_encounter():
    conn = db_connect()
    error = None

    data = json.loads(request.data)
    response = post_encounter(conn, data)

    # check what the response look like
    print("response", response)

    if response <= 0:
        error = 'Unable to post encounter.'

    if error is None:
        return redirect(url_for('index'))
    else:
        return error


@app.route('/getProcessedAudio', methods=['POST'])
def getProcessedAudio():
    data = json.loads(request.data)
    transcription_id = data["transcriptionId"]
    status = checkAudioStatus(transcription_id)

    while status != "completed":
        app.logger.info("request is not completed yet")
        time.sleep(5)
        status = checkAudioStatus(transcription_id)
        if status == "error":
            app.logger.info("request failed")
            return "Error processing transcription"

    if status == "completed":
        result = getTranscriptionResult(transcription_id)
        return result

    return "Text was not processed"

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


def read_file(file_path, chunk_size=5242880):
    # app.logger.info('reading file: ' + file_path)
    with open(file_path, 'rb') as _file:
        while True:
            data = _file.read(chunk_size)
            if not data:
                break
            yield data


def postAudio(transcription_id):
    endpoint = "https://api.assemblyai.com/v2/transcript/" + transcription_id
    headers = {
        "authorization": API_KEY,
    }
    response = requests.get(endpoint, headers=headers)


def checkAudioStatus(transcription_id):
    endpoint = "https://api.assemblyai.com/v2/transcript/" + transcription_id

    headers = {
        "authorization": API_KEY,
    }
    response = requests.get(endpoint, headers=headers)
    json = response.json()
    status = json['status']
    return status


def getTranscriptionResult(transcription_id):
    endpoint = "https://api.assemblyai.com/v2/transcript/" + transcription_id

    headers = {
        "authorization": API_KEY,
    }

    response = requests.get(endpoint, headers=headers)
    json = response.json()
    text = json["text"]
    sentiment_analysis_results = json["sentiment_analysis_results"]
    app.logger.info(json)
    app.logger.info(text)
    app.logger.info(sentiment_analysis_results)
    return { 'text' : text, 'sentiment' : sentiment_analysis_results}

def getSentimentAnalysis(audio_url):
    endpoint = "https://api.assemblyai.com/v2/transcript/"

    headers = {
        "authorization": API_KEY,
        'content-type': 'application/json'
    }

    data = {
        "audio_urk": audio_url,
        "sentiment_analysis": 'true'
    }

    response = requests.get(endpoint, headers=headers, data=data)
    json = response.json()
    text = json["text"]
    app.logger.info(text)


@app.route("/sms", methods=['POST'])
def post_sms():
    conn = db_connect()
    error = None
    client = Client(TWILIO_API_KEY, TWILIO_AUTH_TOKEN)
    data = json.loads(request.data)
    name = data['firstName']
    LName = data['lastName']
    phoneNum = data['number']
    emergencyList = get_emergency_contacts(conn, phoneNum)

    for num in emergencyList:
        client.messages.create(
            body="!! ALERT FROM GUARDIAN !! \n" +
                 name + " " + LName + " started an emergency recording.",
            from_='+14388175458',
            to='+1' + num
        )

    return 'successfully sent SMS to all your emergency numbers'


if __name__ == '__main__':
    app.run(debug=True)

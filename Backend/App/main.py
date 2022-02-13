from db import db_connect, auth_user
from flask import Flask, request, redirect, url_for, flash, session, make_response
from flask_cors import CORS

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
config_path = os.path.join(app.root_path, 'config.yml')
print(config_path)

with open(config_path, "r") as yamlfile:
    data = yaml.load(yamlfile, Loader=yaml.FullLoader)
    print("Read successful")
    print(data["ASSEMBLYAI_API_KEY"])
    API_KEY = data["ASSEMBLYAI_API_KEY"]


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
        user = auth_user(conn, email, password)

        if user[0] == 0:
            error = 'Incorrect Login'

        if error is None:
            # session.clear()
            # session['user_id'] = user['id']
            return redirect(url_for('index'))
        else:
            flash(error)

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
            "audio_url" : audio_url
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

        return 'successfully saved'

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
    app.logger.info(text)

if __name__ == '__main__':
    app.run(debug=True)

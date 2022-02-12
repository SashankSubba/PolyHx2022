import flask
from flask import Flask, request
from flask_cors import CORS
from werkzeug.utils import secure_filename

RECORDING_FOLDER = '/recordings'
ALLOWED_EXTENSIONS = {'mp3'}

app = Flask(__name__)
app.config['RECORDING_FOLDER'] = RECORDING_FOLDER
CORS(app, resources={r"*": {"origins": "*"}})

@app.route("/")
def index():
    return "<p>Hello, World!</p>"

@app.route("/recording", methods=['POST'])
def post_audio():
    # check if the post request has the file part
    print(request)
    if 'file' not in request.files:
        return 'No file part'

    file = request.files['recording']
    if file.filename == '':
            return 'No selected file'

    if file and allowed_file(file.filename):
        recording = request["recording"]
        print(recording)

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
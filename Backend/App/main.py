from db import db_connect, auth_user
from flask import Flask, request, redirect, url_for, flash, session
from flask_cors import CORS
import json

RECORDING_FOLDER = '/recordings'
ALLOWED_EXTENSIONS = {'mp3'}


app = Flask(__name__)
app.config['RECORDING_FOLDER'] = RECORDING_FOLDER
CORS(app, resources={r"*": {"origins": "*"}})


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

if __name__ == '__main__':
    app.run(debug=True)

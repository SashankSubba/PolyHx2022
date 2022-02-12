from db import db_connect, auth_user
from flask import Flask, request, redirect, url_for, flash, session
from flask_cors import CORS

RECORDING_FOLDER = '/recordings'
ALLOWED_EXTENSIONS = {'mp3'}


app = Flask(__name__)
app.config['RECORDING_FOLDER'] = RECORDING_FOLDER
CORS(app, resources={r"*": {"origins": "*"}})


@app.route("/")
def index():
    return "<p>Hello, World!</p>"


@app.route('/login', methods=['GET', 'POST'])
def login():
    conn = db_connect()
    error = None

    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = auth_user(conn, username, password).fetchone()

        if user is None:
            error = 'Incorrect Login'

        if error is None:
            session.clear()
            session['user_id'] = user['id']
            return redirect(url_for('index'))

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

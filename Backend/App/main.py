from db import db_connect, auth_user
from flask import Flask, request, redirect, url_for, flash, session
from flask_cors import CORS


app = Flask(__name__)
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


if __name__ == '__main__':
    app.run(debug=True)

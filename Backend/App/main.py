from db import db_connect, auth_user
from flask import Flask, request, redirect, url_for, flash
from flask_cors import CORS


app = Flask(__name__)
CORS(app)


@app.route("/")
def index():
    return "<p>Hello, World!</p>"


@app.route('/login', methods=['GET', 'POST'])
def login():
    conn = db_connect()

    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = auth_user(conn, username, password)

        if user:
            return redirect(url_for('index'))
        else:
            flash("failure")


if __name__ == '__main__':
    app.run(debug=True)

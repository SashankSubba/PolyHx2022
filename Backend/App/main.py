from flask import Flask, request
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from models import User

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
CORS(app)
db = SQLAlchemy(app)

@app.route("/")
def index():
    return "<p>Hello, World!</p>"

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

if __name__ == '__main__':
   db.create_all()
   app.run(debug = True)

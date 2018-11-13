import os

from flask import Flask, session, render_template, request, Response, jsonify
from flask_socketio import SocketIO, emit
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

app = Flask(__name__)
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")
socketio = SocketIO(app)

# Set up database
engine = create_engine(os.getenv("DATABASE_URL"))
db = scoped_session(sessionmaker(bind=engine))
class Users(db.Model):
    id = db.Column(db.Integer(10))
    """docstring for Users."""
    def __init__(self, arg):
        super(Users, self).__init__()
        self.arg = arg

#user TABLE
db.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER  PRIMARY KEY AUTOINCREMENT, username VARCHAR(20) NOT NULL UNIQUE, lastname VARCHAR(30) NOT NULL, firstname VARCHAR(30) NOT NULL, email VARCHAR(40) NOT NULL UNIQUE, password VARCHAR(80) NOT NULL, admin INTEGER(1) NOT NULL DEFAULT(0))")
#db.execute("INSERT INTO users(username, email, password, admin) VALUES('mike','myckhel1@hotmail.com','january123', 'true')")

@app.route("/")
def index():
    return render_template('home.html')

@app.route("/login")
def login():
    return render_template('login.html')

@app.route("/register", methods=["POST","GET"])
def register():
    if request.form.get('username'):
        firstname = request.form.get('firstname')
        lastname = request.form.get('lastname')
        email = request.form.get('email')
        username = request.form.get('username')
        password = request.form.get('password')
        try:
            user = db.execute(f"INSERT INTO users(username,firstname,lastname,email,password) VALUES('{username}','{firstname}','{lastname}','{email}','{password}')")
            print(user)
        except Exception as e:
            print(e)
            error = {'e': 'internal server error'}
            return jsonify(error)
        status = {'status': 'true', 'form': request.form}
        return jsonify(status)
    return render_template('register.html')

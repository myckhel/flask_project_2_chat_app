import os
from models import User

from flask import Flask, session, render_template, request, Response, jsonify
from flask_socketio import SocketIO, emit
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from werkzeug.security import check_password_hash, generate_password_hash

app = Flask(__name__)
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")
socketio = SocketIO(app)
# Set up database
# engine = create_engine(os.getenv("DATABASE_URL"))
# db = scoped_session(sessionmaker(bind=engine))
#user TABLE
#db.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER  PRIMARY KEY AUTOINCREMENT, username VARCHAR(20) NOT NULL UNIQUE, lastname VARCHAR(30) NOT NULL, firstname VARCHAR(30) NOT NULL, email VARCHAR(40) NOT NULL UNIQUE, password VARCHAR(80) NOT NULL, admin INTEGER(1) NOT NULL DEFAULT(0))")
#db.execute("INSERT INTO users(username, email, password, admin) VALUES('mike','myckhel1@hotmail.com','january123', 'true')")

@app.route("/")
def index():
    return render_template('home.html')

@app.route("/login")
def login():
    return render_template('login.html')

#check_password_hash(rows[0]["hash"], request.form.get("password")
@app.route("/register", methods=["POST","GET"])
def register():
    return render_template('register.html')

@app.route("/auth", methods=["POST"])
def auth():
    if request.form.get('action') == 'register':
        firstname = request.form.get('firstname')
        lastname = request.form.get('lastname')
        email = request.form.get('email')
        username = request.form.get('username')
        password = generate_password_hash(request.form.get('password'))#, method="pbkdf2:sha256", salt_length=8)
        try:
            user = User(username=username,firstname=firstname, lastname=lastname, email=email, password=password)
            db.add(user)
            db.commit()
            #user = db.execute(f"INSERT INTO users(username,firstname,lastname,email,password) VALUES('{username}','{firstname}','{lastname}','{email}','{password}')")
            print(user)
        except Exception as e:
            print(e)
            error = {'e': 'internal server error'}
            return jsonify(error)
        status = {'status': 'true', 'form': request.form}
        return jsonify(status)

    if request.form.get('action') == 'login':
        login = request.form.get('login')
        user = User.query.filter_by(username=login).first()
        # user = User.query.filter((User.username == login) or (User.email == login)).first()
        if user:
            password = check_password_hash(user.password, request.form.get('password'))
            if password:
                return jsonify({'status': 'true', 'password': user.password, 'username': user.username})
            else:
                return jsonify({'status': 'false', 'reason': 'password not correct'})
        else:
            return jsonify({'status': 'false', 'reason': 'username not exists'})
    return jsonify({'status': 'false', 'reason': 'request not allowed'})

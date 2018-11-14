from flask_sqlalchemy import SQLAlchemy
from flask import Flask

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///chat.db" #os.getenv("DATABASE_URL")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
# db.init_app(app)
db = SQLAlchemy(app)

class User(db.Model):
    """docstring for ."""
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(21), unique=True, nullable=False)
    lastname = db.Column(db.String(30), nullable=False)
    firstname = db.Column(db.String(30), nullable=False)
    email = db.Column(db.String(40), unique=True, nullable=False)
    password = db.Column(db.String(80), nullable=False)
    admin = db.Column(db.Integer(), nullable=False, default=0)

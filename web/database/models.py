from flask_sqlalchemy import SQLAlchemy
from web.flaskapp import db
from flask import Flask

app = Flask(__name__)

# Also for run through flask_main, remove point before flaskapp 

class User(db.Model):
    __tablename__ = "users"
    user_id = db.Column(db.Integer, primary_key=True) 
    login = db.Column(db.String(255), unique=True, nullable=False)
    user_fname = db.Column(db.String(255))
    user_sname = db.Column(db.String(255))
    password = db.Column(db.String(255), nullable=False)

    user_files = db.relationship("File", back_populates = "owner", cascade="all, delete-orphan")


    def __repr__(self) -> str:
        return f"User(user_id {self.user_id!r}, name={self.user_fname!r}, surname={self.user_fname!r})"


class File(db.Model):
    __tablename__ = "files"
    file_id = db.Column(db.Integer, primary_key = True)
    file_name = db.Column(db.String(255), nullable = False)
    file_owner = db.Column(db.Integer, db.ForeignKey("users.user_id"), nullable = False)

    owner = db.relationship("User", back_populates="user_files")

    def __repr__(self) -> str:
        return f"File(file_id={self.file_id!r}, name={self.file_name!r}, ownner={self.file_owner!r})"

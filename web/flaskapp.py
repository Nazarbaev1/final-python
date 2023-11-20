from flask_sqlalchemy import SQLAlchemy
from flask import Flask

db = SQLAlchemy()

app = Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI'] = r'sqlite:///C:\Users\Yeldos\Desktop\University\course 2\Adv Python\cinema\web\dbase.db' # You have to replace the database path here with your own :) 

app.config['SECRET_KEY']="my secret key here"
db.init_app(app)

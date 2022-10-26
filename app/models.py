from datetime import datetime
from app import db


#create a user class that inherits from the db.model
#Create table user

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(50), nullable = False, unique=True)
    username = db.Column(db.String(50), nullable = False, unique=True)
    password = db.Column(db.String(256), nullable=False)
    date_created = db.Column(db.DateTime, nullable = False, default = datetime.utcnow)
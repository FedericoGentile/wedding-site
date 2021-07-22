from datetime import datetime
from flask import current_app
from wedsite import db

class Response(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=False, nullable=False)
    lastname = db.Column(db.String(20), unique=False, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    adults = db.Column(db.Integer, unique=False, nullable=False, default=0)
    children = db.Column(db.Integer, unique=False, nullable=False, default=0)
    message = db.Column(db.Text, unique=False, nullable=True)
    accomodation = db.Column(db.Boolean, unique=False, default=False, nullable=True)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __repr__(self):
        return f"Response('{slef.username}', '{self.lastname}')"
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import DateTime
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from datetime import datetime

db = SQLAlchemy()

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(40), nullable=False)
    email = db.Column(db.String(50), unique=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)
    
    def __repr__(self):
        return f'User -->{self.email}'
    
    def set_password_hash(self, password):
        self.password_hash = generate_password_hash(password=password)
        
    def check_password_hash(self, password):
        return check_password_hash(pwhash=self.password_hash, password=password)
    

class Plan(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    user = db.relationship('User', backref=db.backref('plans', lazy=True))
    description = db.Column(db.String(50), nullable=False)
    planningDate = db.Column(DateTime, default=datetime.now) 
    
from datetime import datetime
from flask_login import UserMixin
from app import db

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(256), nullable=False)
    name = db.Column(db.String(100), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    health_data = db.relationship('HealthData', backref='user', lazy=True)
    diabetes_data = db.relationship('DiabetesData', backref='user', lazy=True)

class HealthData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    blood_pressure = db.Column(db.String(10))
    heart_rate = db.Column(db.Integer)
    temperature = db.Column(db.Float)
    weight = db.Column(db.Float)
    risk_score = db.Column(db.Float)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
    cholesterol = db.Column(db.Float)

class DiabetesData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    gender = db.Column(db.String(10))
    age = db.Column(db.Float)
    hypertension = db.Column(db.Boolean)
    heart_disease = db.Column(db.Boolean)
    smoking_history = db.Column(db.String(20))
    bmi = db.Column(db.Float)
    hba1c_level = db.Column(db.Float)
    blood_glucose_level = db.Column(db.Float)
    risk_score = db.Column(db.Float)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
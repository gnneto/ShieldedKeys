from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)
    nome = db.Column(db.String(100))
    sobrenome = db.Column(db.String(100))
    email = db.Column(db.String(255), unique=True, nullable=False)
    data_aniversario = db.Column(db.Date)
    numero_telefone = db.Column(db.String(20))
    creation_date_account = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}')"

class Password(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    site_name = db.Column(db.String(100), nullable=False)
    username = db.Column(db.String(100))
    password_hash = db.Column(db.String(255), nullable=False)
    security_phrase = db.Column(db.String(255), nullable=False)
    url = db.Column(db.String(255))
    creation_date = db.Column(db.DateTime, default=datetime.utcnow)
    update_date = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    user = db.relationship('User', backref=db.backref('passwords', lazy=True))

    def check_security_phrase(self, security_phrase):
        return self.security_phrase == security_phrase
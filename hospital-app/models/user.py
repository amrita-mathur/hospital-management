from db import db

class UserModel(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    username = db.Column(db.String(200), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False, load_only=True)
    age = db.Column(db.Integer, nullable=False)
    type = db.Column(db.String(10), nullable=False)
    gender = db.Column(db.String(10), nullable=False)
    contact = db.Column(db.String(15), unique=True, nullable=False)
    # patient = db.relationship('PatientModel', back_populates='user', lazy="dynamic", uselist=False)
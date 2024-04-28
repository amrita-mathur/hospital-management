from db import db

class PatientModel(db.Model):
    __tablename__ = "patients"

    id = db.Column(db.Integer, primary_key=True)
    userId = db.Column(db.Integer, db.ForeignKey("users.id"), unique=True, nullable=False)
    medical_history = db.Column(db.PickleType)
    appointment_records = db.Column(db.PickleType)
    
from db import db

class DoctorPatientModel(db.Model):
    __tablename__ = "doctor_patient"

    id = db.Column(db.Integer, primary_key=True)
    doctor_id = db.Column(db.Integer, db.ForeignKey("doctors.id"), unique=False)
    patient_id = db.Column(db.Integer, db.ForeignKey("patients.id"))
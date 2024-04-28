from db import db

class DoctorModel(db.Model):
    __tablename__ = "doctors"

    id = db.Column(db.Integer, primary_key=True)
    userId = db.Column(db.Integer, db.ForeignKey("users.id"), unique=True, nullable=False)
    specialization = db.Column(db.String(200))
    availability_schedule = db.Column(db.PickleType)
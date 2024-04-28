from db import db


class DepartmentDoctorModel(db.Model):
    __tablename__ = "department_doctor"

    id = db.Column(db.Integer, primary_key=True)
    department_id = db.Column(db.Integer, db.ForeignKey("departments.id"))
    doctor_id = db.Column(db.Integer, db.ForeignKey("doctors.id"))


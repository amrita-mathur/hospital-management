from db import db

class DepartmentModel(db.Model):
    __tablename__ = "departments"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), unique=True, nullable = False)
    services_offered = db.Column(db.PickleType)
    
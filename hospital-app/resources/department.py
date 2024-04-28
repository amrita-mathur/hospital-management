import uuid
from flask import request, jsonify
from flask.views import MethodView
from flask_smorest import Blueprint, abort
# from db import departments
from schemas import DepartmentSchema, DepartmentUpdateSchema, AddDoctorSchema
from db import db
from models import DepartmentModel, DepartmentDoctorModel
from sqlalchemy.exc import SQLAlchemyError, IntegrityError

blp = Blueprint("Departments", "departments", description="Operations on departments")


@blp.route("/departments/<int:id>")
class Department(MethodView):

    @blp.response(200, DepartmentSchema)
    def get(self, id):
        department = DepartmentModel.query.get_or_404(id)
        return department

    def delete(self, id):
        department = DepartmentModel.query.get_or_404(id)
        raise NotImplementedError("Deleting the department is not implemented.")

    @blp.arguments(DepartmentUpdateSchema)
    @blp.response(200, DepartmentSchema)
    def put(self, updated_department, id):
        department = DepartmentModel.query.get(id)
        if department:
            department.name = updated_department["name"]
            department.services_offered = updated_department["services_offered"]
        # else:
        #     department = DepartmentModel(id=id, **updated_department)    
        
        db.session.add(department)
        db.session.commit()

        
@blp.route('/departments')
class DepartmentList(MethodView):
      
    @blp.response(200, DepartmentSchema(many=True))  
    def get(self):
       return DepartmentModel.query.all()

    @blp.arguments(DepartmentSchema)
    @blp.response(201, DepartmentSchema)
    def post(self, new_department):
        print(new_department)
        department = DepartmentModel(**new_department)
        try:
            db.session.add(department)
            db.session.commit()
        except IntegrityError:
            abort(400, message= "A department with same name exists")
        except SQLAlchemyError:
            abort(500, message="An error occurred while inserting department")

        return department
    
@blp.route('/adddoctor')    
class AddDoctor(MethodView):

    @blp.arguments(AddDoctorSchema)
    @blp.response(201,AddDoctorSchema)
    def post(self, department_doctor_data):
        department_doctor = DepartmentDoctorModel(**department_doctor_data)
        try:
            db.session.add(department_doctor)
            db.session.commit()
        except SQLAlchemyError:
            abort(500, message="An error occurred while inserting department")

        return department_doctor




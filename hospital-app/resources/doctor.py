import uuid
import pdb
from flask import request, jsonify
from flask.views import MethodView
from flask_smorest import Blueprint, abort
# from db import doctors
from schemas import DoctorSchema, DoctorUpdateSchema, AddPatientSchema, GetDoctorsByDeptResponse
from db import db
from models import DoctorModel, DoctorPatientModel, DepartmentDoctorModel, UserModel
from sqlalchemy.exc import SQLAlchemyError, IntegrityError

blp = Blueprint("Doctors", "doctors", description="Operations on doctors")


@blp.route("/doctors/<int:id>")
class Doctor(MethodView):

    @blp.response(200, DoctorSchema)
    def get(self, id):
        doctor = DoctorModel.query.get_or_404(id)
        return doctor

    def delete(self, id):
        doctor = DoctorModel.query.get_or_404(id)
        raise NotImplementedError("Deleting the doctor is not implemented.")

    @blp.arguments(DoctorUpdateSchema)
    @blp.response(200, DoctorSchema)
    def put(self, updated_doctor, id):
        doctor = DoctorModel.query.get(id)
        if doctor:
            doctor.medical_history = updated_doctor["medical_history"]
            doctor.appointment_records = updated_doctor["appointment_records"]
        else:
            doctor = DoctorModel(id=id, **updated_doctor)    
        
        db.session.add(doctor)
        db.session.commit()

        
@blp.route('/doctors')
class DoctorList(MethodView):
      
    @blp.response(200, DoctorSchema(many=True))  
    def get(self):
       print(DoctorModel.query.all())
       return DoctorModel.query.all()

    @blp.arguments(DoctorSchema)
    @blp.response(201, DoctorSchema)
    def post(self, new_doctor):
        print(new_doctor)
        doctor = DoctorModel(**new_doctor)
        try:
            db.session.add(doctor)
            db.session.commit()
        except IntegrityError:
            abort(400, message= "A doctor with same name exists")
        except SQLAlchemyError:
            abort(500, message="An error occurred while inserting doctor")

        return doctor
    
@blp.route('/addpatient')    
class AddPatient(MethodView):

    @blp.arguments(AddPatientSchema)
    @blp.response(201,AddPatientSchema)
    def post(self, doctor_patient_data):
        doctor_patient = DoctorPatientModel(**doctor_patient_data)
        try:
            db.session.add(doctor_patient)
            db.session.commit()
        except SQLAlchemyError:
            abort(500, message="An error occurred while inserting doctor")

        return doctor_patient

@blp.route('/removepatient/<int:doctor_id>/<int:patient_id>')    
class RemovePatient(MethodView):

    def post(self, doctor_id,patient_id):
        doctor_patient = DoctorPatientModel.query.filter_by(doctor_id=doctor_id, patient_id = patient_id).first()
        print(doctor_patient)
        try:
            db.session.delete(doctor_patient)
            db.session.commit()
        except SQLAlchemyError:
            abort(500, message="An error occurred while deleting doctor")

        return {"message":"Patient successfully removed."}, 200


@blp.route('/getdoctors/<int:deptid>')    
class GetDoctorsByDept(MethodView):
    @blp.response(200, GetDoctorsByDeptResponse)
    def get(self, deptid):
        try:
            department_doctors = DepartmentDoctorModel.query.filter_by(department_id = deptid).all()
            print(department_doctors)
            doctor_list = []
            for doctor in department_doctors:
                print("doctor_id", doctor.doctor_id)
                doctor_dict = {}
                doctor_id = doctor.doctor_id
                doctor_dict['doctor_id'] = doctor_id
                user_id = DoctorModel.query.filter_by(id = doctor_id).first().userId
                user_name = UserModel.query.filter_by(id=user_id).first().name
                doctor_dict['doctor_name'] = user_name
                print("doctor_dict", doctor_dict)

                doctor_list.append(doctor_dict)    
            print(doctor_list)
            return {"doctors" : doctor_list }
        except SQLAlchemyError:
            abort(500, "Not able to find doctors")

@blp.route('/getdoctors/<string:availability>')    
class GetDoctorsByAvailability(MethodView):
    @blp.response(200, GetDoctorsByDeptResponse)
    def get(self, availability):
        # pdb.set_trace()
        print("Availability", availability)
        doctors = DoctorModel.query.all()

        print("doctors", doctors)
        doctor_list = []
        for doctor in doctors:
            if availability in doctor.availability_schedule:
                doctor_dict = {}
                doctor_id = doctor.id
                doctor_dict['doctor_id'] = doctor_id
                user_id = DoctorModel.query.filter_by(id = doctor_id).first().userId
                user_name = UserModel.query.filter_by(id=user_id).first().name
                doctor_dict['doctor_name'] = user_name
                print("doctor_dict", doctor_dict)

                doctor_list.append(doctor_dict)    
            print("doctor_list", doctor_list)
        return {"doctors" : doctor_list }
    # except SQLAlchemyError:
    #     abort(500, "Not able to find doctors with such specialization.")             

@blp.route('/getdoctorsBySp/<string:specialization>')    
class GetDoctorsBySpecialization(MethodView):
    @blp.response(200, GetDoctorsByDeptResponse)
    def get(self, specialization):
        try:
            specialized_doctors = DoctorModel.query.filter_by(specialization=specialization).all()
            print(specialized_doctors)
            doctor_list = []
            for doctor in specialized_doctors:
                print("doctor_id", doctor.id)
                doctor_dict = {}
                doctor_id = doctor.id
                doctor_dict['doctor_id'] = doctor_id
                user_id = DoctorModel.query.filter_by(id = doctor_id).first().userId
                user_name = UserModel.query.filter_by(id=user_id).first().name
                doctor_dict['doctor_name'] = user_name
                print("doctor_dict", doctor_dict)

                doctor_list.append(doctor_dict)    
            print(doctor_list)
            return {"doctors" : doctor_list }
        except SQLAlchemyError:
            abort(500, "Not able to find doctors with such specialization.") 

     
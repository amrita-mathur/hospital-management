import uuid
from flask import request, jsonify
from flask.views import MethodView
from flask_smorest import Blueprint, abort
# from db import patients
from schemas import PatientSchema, PatientUpdateSchema, GetPatientsByDoctorResponse
from db import db
from models import PatientModel, DoctorPatientModel, UserModel
from sqlalchemy.exc import SQLAlchemyError, IntegrityError

blp = Blueprint("Patients", "patients", description="Operations on patients")


@blp.route("/patients/<int:id>")
class Patient(MethodView):

    @blp.response(200, PatientSchema)
    def get(self, id):
        patient = PatientModel.query.get_or_404(id)
        return patient

    def delete(self, id):
        patient = PatientModel.query.get_or_404(id)
        raise NotImplementedError("Deleting the patient is not implemented.")

    @blp.arguments(PatientUpdateSchema)
    @blp.response(200, PatientSchema)
    def put(self, updated_patient, id):
        patient = PatientModel.query.get(id)
        if patient:
            patient.medical_history = updated_patient["medical_history"]
            patient.appointment_records = updated_patient["appointment_records"]
        else:
            patient = PatientModel(id=id, **updated_patient)    
        
        db.session.add(patient)
        db.session.commit()

        
@blp.route('/patients')
class PatientList(MethodView):
      
    @blp.response(200, PatientSchema(many=True))  
    def get(self):
       return PatientModel.query.all()

    @blp.arguments(PatientSchema)
    @blp.response(201, PatientSchema)
    def post(self, new_patient):
        print(new_patient)
        patient = PatientModel(**new_patient)
        try:
            db.session.add(patient)
            db.session.commit()
        except IntegrityError:
            abort(400, message= "A patient with same name exists")
        except SQLAlchemyError:
            abort(500, message="An error occurred while inserting patient")

        return patient, 201 
    
@blp.route('/getpatients/<int:doctor_id>')    
class GetPatientsByDoctor(MethodView):
    @blp.response(200, GetPatientsByDoctorResponse)
    def get(self, doctor_id):
        try:
            patients = DoctorPatientModel.query.filter_by(doctor_id = doctor_id).all()
            print(patients)
            patient_list = []
            for patient in patients:
                
                patient_dict = {}
                patient_id = patient.patient_id
                patient_dict['patient_id'] = patient_id
                user_id = PatientModel.query.filter_by(id = patient_id).first().userId
                user_name = UserModel.query.filter_by(id=user_id).first().name
                patient_dict['patient_name'] = user_name
                print("patient_dict", patient_dict)

                patient_list.append(patient_dict)    
            print(patient_list)
            return {"patients" : patient_list }
        except SQLAlchemyError:
            abort(500, "Not able to find patients")



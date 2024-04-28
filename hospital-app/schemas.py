from marshmallow import Schema, fields

class UserSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    username = fields.Str(required=True)
    password = fields.Str(required=True)
    age = fields.Int(required=True)
    type = fields.Str(required=True)
    gender = fields.Str(required=True)
    contact = fields.Str(required=True)

class LoginSchema(Schema):
    username = fields.Str(required=True)
    password = fields.Str(required=True)    

class UserUpdateSchema(Schema):
    username = fields.Str()
    password = fields.Str()
    name = fields.Str()
    age = fields.Int()
    type = fields.Str()
    gender = fields.Str()
    contact = fields.Str()

class PatientSchema(Schema):
    id = fields.Int(dump_only=True)
    userId = fields.Int(required=True)
    medical_history = fields.Dict(keys=fields.Str())
    appointment_records = fields.List(fields.Dict())

class PatientUpdateSchema(Schema):
    medical_history = fields.Dict()   
    appointment_records = fields.List(fields.Dict()) 

class DoctorSchema(Schema):
    id = fields.Int(dump_only=True)
    userId = fields.Int(required=True)
    specialization = fields.Str(required=True)
    availability_schedule = fields.List(fields.Str(),required=True)

class DoctorUpdateSchema(Schema):
    specialization = fields.Str()
    availability_schedule = fields.List(fields.Str())
    
class AddPatientSchema(Schema):
    id = fields.Int(dump_only=True)
    doctor_id = fields.Int(required=True)  
    patient_id = fields.Int(required=True)

class DepartmentSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    services_offered = fields.List(fields.Str())

class DepartmentUpdateSchema(Schema):
    name = fields.Str()
    services_offered = fields.List(fields.Str())

class AddDoctorSchema(Schema):
    id = fields.Int(dump_only=True)
    doctor_id = fields.Int(required=True)  
    department_id = fields.Int(required=True)    


class GetDoctorsByDeptResponse(Schema):
    doctors = fields.List(fields.Dict(), required=True)    
        
class GetPatientsByDoctorResponse(Schema):
    patients = fields.List(fields.Dict(), required=True)    
        

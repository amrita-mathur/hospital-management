# users = {
#     1: {
#      "id": 1,   
#      "name": "John",
#      "age": 60,
#      "type": "patient",
#      "gender": "Male",
#      "contact": "9852621721"  
#     },
#     2: {
#      "id": 2,   
#      "name": "Jack",
#      "age": 12,
#      "type": "patient",
#      "gender": "Male",
#      "contact": "9852621721"  
#     },
#     3: {
#      "id": 3,   
#      "name": "Mary",
#      "age": 45,
#      "type": "doctor",
#      "gender": "Female",
#      "contact": "9852621721"  
#     },
#     4: {
#      "id": 4,   
#      "name": "Albert",
#      "age": 26,
#      "type": "doctor",
#      "gender": "Male",
#      "contact": "9852621721"  
#     },
    

# }

# patients = {
#     1: {
#         "id": 1,
#         "userId": 1,
#         "medical_history": {
# "previous_diagnoses": '''
# Hypertension (diagnosed in 2015)
# Managed with medication (Lisinopril, 10mg daily)
# Regular blood pressure monitoring every six months
# Type 2 Diabetes Mellitus (diagnosed in 2017)
# Managed with diet, exercise, and medication (Metformin, 500mg twice daily)
# Annual A1C checks to monitor glucose control
# Hyperlipidemia (diagnosed in 2016)
# Managed with medication (Atorvastatin, 20mg daily)
# Lipid profile checked annually ''',
# "allergies":
# '''Penicillin
# Patient experiences rash and itching upon exposure
# Shellfish
# Patient experiences severe allergic reaction (anaphylaxis)''',
# "medications":'''
# Lisinopril (10mg daily) - for hypertension
# Metformin (500mg twice daily) - for type 2 diabetes mellitus
# Atorvastatin (20mg daily) - for hyperlipidemia
# Aspirin (81mg daily) - for cardiovascular protection
# Albuterol inhaler (as needed) - for asthma
# Loratadine (10mg daily) - for seasonal allergies '''
#         },
# "appointment_records": [
#     {
#         "appointment_date": "2024-04-26",
#         "appointment_time": "10:00 AM",
#         "doctor": "Dr. Mary",
#         "reason_for_visit": "Annual check-up"
#     },
#     {
#         "appointment_date": "2024-04-28",
#         "appointment_time": "02:30 PM",
#         "doctor": "Dr. Albert",
#         "reason_for_visit": "Follow-up for hypertension"
#     }
# ]                           
#     },
#     2: {
#         "id": 2,
#         "userId": 2,
#         "medical_history": {
#             "previous_diagnosis": '''Asthma (diagnosed in childhood)
# Managed with rescue inhaler (Albuterol) as needed
# Annual pulmonary function tests (PFTs) to monitor lung function
# Major Depressive Disorder (diagnosed in 2018)
# Managed with psychotherapy and medication (Sertraline, 50mg daily)
# Regular follow-ups with a psychiatrist for monitoring and adjustment of treatment
# Migraine headaches (diagnosed in 2015)
# Managed with medication (Sumatriptan) for acute episodes
# Lifestyle modifications to identify triggers and reduce frequency''',
#             "allergies": '''Penicillin
# Patient experiences hives and swelling upon exposure
# Latex
# Patient experiences itching and redness upon contact''',
#             "medications": '''Sertraline (50mg daily) - for major depressive disorder
# Sumatriptan (as needed) - for migraine headaches
# Albuterol inhaler (as needed) - for asthma
# Loratadine (10mg daily) - for seasonal allergies
# Ibuprofen (as needed) - for pain relief
# Melatonin (3mg nightly) - for sleep disturbances'''
#         },
#     "appointment_records": [
#     {
#         "appointment_date": "2024-05-02",
#         "appointment_time": "09:15 AM",
#         "doctor": "Dr. Mary",
#         "reason_for_visit": "Asthma Examination"
#     },
#     {
#         "appointment_date": "2024-05-03",
#         "appointment_time": "11:00 AM",
#         "doctor": "Dr. Albert",
#         "reason_for_visit": "Annual physical examination"
#     }
# ]    

#     }
# }

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
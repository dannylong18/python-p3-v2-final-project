# lib/helpers.py
from models.patient import Patient
from models.treatment import Treatment

def list_patients():
    patients = Patient.get_all_patients()
    for patient in patients:
        print(patient)

def find_patient_by_name():
    name = input("Enter the patient's first and last name: ")
    patient = Patient.find_patient_by_name(name)

    print(patient) if patient else print (f'Patient {name} not found')



def exit_program():
    print("Goodbye!")
    exit()


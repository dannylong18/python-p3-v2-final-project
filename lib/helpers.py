# lib/helpers.py
from models.patient import Patient
from models.treatment import Treatment

def list_patients():
    patients = Patient.get_all_patients()
    for patient in patients:
        print(patient)





def exit_program():
    print("Goodbye!")
    exit()


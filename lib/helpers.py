# lib/helpers.py
from models.patient import Patient
from models.treatment import Treatment

def list_patients():
    patients = Patient.get_all_patients()
    for patient in patients:
        print(patient)

def find_patient_by_name():
    name = input("*** Enter the patient's first and last name: ")
    patient = Patient.find_patient_by_name(name)

    print(patient) if patient else print (f'Patient {name} not found')

def create_patient():
    name = input("*** Enter patient's first and last name: ")
    birthday = input("*** Enter patient's date of birth (Example: March 22, 1995 >> 03221995): ")
    insurance = input("*** Enter patient's insurance: ")
    treatment_id = input("*** Enter patient's treatment id (Type '1' for Physical Therapy; '2' for Pain Management; '3' for Surgery): )")

    try:
        patient = Patient.create_patient(name, birthday, insurance, treatment_id)
        print(f'Sucessfully created new patient!')
    
    except Exception as exc:
        print(f'Error creating patient, please start again: ', exc)



def exit_program():
    print("Goodbye!")
    exit()


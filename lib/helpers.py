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
        print(f'Sucessfully created new patient! --> {patient}')

    except Exception as exc:
        print(f'Error creating patient, please start again: ', exc)

def update_patient_information():
    pt_name = input("*** Enter the patient's first and last name: ")
    if patient := Patient.find_patient_by_name(pt_name):
        try:
            name = input("*** Enter patient's new first and last name: ")
            patient.name = name

            birthday = input("*** Enter patient's date of birth (Example: March 22, 1995 >> 03221995): ")
            patient.birthday = birthday

            insurance = input("*** Enter patient's insurance: ")
            patient.insurance = insurance

            treatment_id = input("*** Enter patient's treatment id (For patient in Physical Therapy, type '1'; in Pain Management, type '2'; undergoing surgery, type '3'): )")
            treatment_id = int(treatment_id)
            patient.treatment_id = treatment_id

            patient.update_patient()

        except Exception as exc:
            print("Error updating patient, please try again: ", exc)
    
    else: print(f"Patient {pt_name} not found")

def delete_patient():
    pt_name = input("Enter patient's name: ")
    if patient := Patient.find_patient_by_name(pt_name)
        patient.delete_patient()
        print(f"Patient {pt_name} deleted")
    
    else: print(f"Patient {pt_name} not found")

def list_patients_in_treatment():
        treat_id = input("*** To list patients in: Physical Therapy, type '1'; Pain Management, type '2'; undergoing surgery, type '3'): )")
        treat_id = int(treat_id)
        if treatment_id := Treatment.find_treatment_by_id(treat_id):
            for patient in treatment_id.patients():
                print(patient)

        else: print(f"Treatment {treat_id} does not exist"
                    )
            
def exit_program():
    print("Goodbye!")
    exit()


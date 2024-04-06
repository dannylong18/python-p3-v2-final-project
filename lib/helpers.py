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
    print()
    print(patient) if patient else print (f'Patient {name} not found')

def create_patient():
    name = input("*** Enter patient's first and last name: ")

    birthday = input("""*** Enter patient's date of birth
    (Example: if birthday is March 22, 1995 >> Enter '03/22/1995') 
        --> : """)
    
    insurance = input("*** Enter patient's insurance: ")

    list_treatments()
    print()
    treatment_id = input("*** Enter number from treatment list above -->:")
    treatment_id = int(treatment_id)

    try:
        patient = Patient.create_patient(name, birthday, insurance, treatment_id)
        print(f'Sucessfully created new patient! --> {patient}')

    except Exception as exc:
        print(f'Error creating patient, please start again: ', exc)

def update_patient_information():
    pt_id = input("*** Enter the number of the patient you would like to update:")
    if patient := Patient.find_patient_by_id(pt_id):
        try:
            name = input("*** Enter patient's new first and last name: ")
            patient.name = name

            birthday = input("""*** Enter patient's date of birth 
    (Example: March 22, 1995 >> '03/22/1995') 
        --> : """)
            patient.birthday = birthday

            insurance = input("*** Enter patient's insurance: ")
            patient.insurance = insurance

            list_treatments()
            treatment_id = input("""*** Enter number from treatment list above: 
        --> : """)
            treatment_id = int(treatment_id)
            patient.treatment_id = treatment_id

            patient.update_patient()
            print()
            print(f"Patient {pt_id} updated! --> {patient}")

        except Exception as exc:
            print("Error updating patient, please try again: ", exc)
    
    else: print(f"Patient {pt_name} not found")

def delete_patient():
    pt_id = input("*** Enter the number of the patient you would like to delete:")
    patient = Patient.find_patient_by_id(pt_id)
    if patient:
        patient.delete_patient_from_db()
        print()
        print(f"Patient {pt_id} deleted")

        remaining_pts = Patient.get_all_patients()

        for index, patient in enumerate(remaining_pts, start=1):
            patient.id = index
            patient.update_patient()

    else: print(f"Patient {pt_id} not found")





def list_treatments():
    treatments = Treatment.get_all_treatments()
    for treatment in treatments:
        print(treatment)

def find_treatment_by_name():
    name = input("*** Enter treatment option ('physical therapy'; 'pain management'; 'surgery'): ")
    treatment = Treatment.find_treatment_by_name(name)

    print(treatment) if treatment else print (f'Treatment {name} not found')

def create_treatment():
    name = input("*** Enter treatment name: ")
    duration = input("""
*** Enter duration of treatment in weeks 
(For example, 3 months = 12 weeks; so enter 12):""")
    duration = int(duration)

    try:
        treatment = Treatment.create_treatment(name, duration)
        print(f'Sucessfully created new treatment! --> {treatment}')

    except Exception as exc:
        print(f'Error creating treatment, please start again: ', exc)

def update_treatment_information():
    treatment_id = input("*** Enter the number above corresponding to the treatment to update: ")
    if treatment := Treatment.find_treatment_by_id(treatment_id):
        try:
            name = input("*** Enter a new name for the treatment: ")
            treatment.name = name

            duration = input("""*** Enter new duration of treatment in weeks 
    (For example, 3 months = 12 weeks; so enter 12) 
        --> : """)
            duration = int(duration) 
            treatment.duration = duration

            treatment.update_treatment()
            print(f"""
 ***Treatment successfully updated! --> {treatment}""")

        except Exception as exc:
            print("Error updating treatment, please try again: ", exc)
    
    else: print(f"Treatment {treatment_id} not found")

def delete_treatment():
    treat_id = input("""
                    
*** To delete treatment, enter corresponding number for treatment above; 
    or enter 0 to return to main menu:
                    
    --> : """)
    
    treatment = Treatment.find_treatment_by_id(int(treat_id))

    if not treatment:
        print(f"Treatment {treat_id} not found")
        return 
    
    patients = treatment.patients()

    treatment.delete_treatment_from_db()
    print(f"***Treatment {treat_id} deleted")

    if patients:
        for patient in patients:
            patient.treatment_id = None
            patient.update_patient()

def list_patients_in_treatment():
        treat_id = input("""
                         
    *** To view patients, enter number of desired treatment above: 
                         
            --> : """)
        treat_id = int(treat_id)
        treatment = Treatment.find_treatment_by_id(treat_id)
        if treatment:
            patients = treatment.patients()
            if patients:
                for patient in patients:
                    print()
                    print(patient)
            
            else: print("No patients undergoing this treatment at this time")
       
        else: print(f"treatment {treat_id} does not exist")
            
def exit_program():
    print("""
          
          Exiting program...Goodbye!
          
          """)
    exit()


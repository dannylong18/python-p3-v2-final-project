# lib/helpers.py
from models.patient import Patient
from models.treatment import Treatment

def list_patients():
    patients = Patient.get_all_patients()
    for i, patient in enumerate(patients, start=1):
        treatment = Treatment.all.get(patient.treatment_id, None)
        print(f'{i}. Name: {patient.name}, DOB: {patient.birthday}, Insurance: {patient.insurance}, undergoing {treatment.name} treatment')
    return patients

def find_patient_by_name():
    print()
    name = input("*** Enter the patient's first and last name (Case Sensitive): ")
    patient = Patient.find_patient_by_name(name)
    print()
    if patient:
        treatment = Treatment.all.get(patient.treatment_id, None)
        print(f'Name: {patient.name}, DOB: {patient.birthday}, Insurance: {patient.insurance}, undergoing {treatment.name} treatment')
    else:
        print(f'Patient {name} not found')

def create_patient():
    name = input("*** Enter patient's first and last name: ")

    birthday = input("""*** Enter patient's date of birth
(Example: if birthday is March 22, 1995 >> Enter '03/22/1995') 
    --> : """)
    
    insurance = input("*** Enter patient's insurance: ")
    print()
    list_treatments()
    print()
    treatment_id = input("*** Enter number from treatment list above -->:")
    treatment_id = int(treatment_id)

    try:
        patient = Patient.create_patient(name, birthday, insurance, treatment_id)
        treatment = Treatment.all.get(patient.treatment_id, None)
        print()
        print(f'Sucessfully created new patient! --> Name: {patient.name}, DOB: {patient.birthday}, Insurance: {patient.insurance}, undergoing {treatment.name} treatment')

    except Exception as exc:
        print(f'Error creating patient, please start again:', exc)

def update_patient_information():
    patients = list_patients()
    print()
    selected_patient = input("*** Enter the number of the patient you would like to update:")
    #patient = patients[int(selected_patient) - 1]
    
    try:
            selected_index = int(selected_patient) - 1
            if selected_index >= 0 and selected_index < len(patients):
                patient = patients[selected_index]
                treatment = Treatment.all.get(patient.treatment_id, None)
                if patient:
                    try:
                        print(f"""
        Patient chosen --> Name: {patient.name}, DOB: {patient.birthday}, Insurance: {patient.insurance}, undergoing {treatment.name} treatment""")
                        print()
                        name = input("*** Enter patient's new first and last name or press 'Enter/Return' to keep current information: ")
                        if name: 
                            patient.name = name

                        birthday = input("""*** Enter patient's date of birth or press 'Enter/Return' to keep current information
            (Example: March 22, 1995 >> '03/22/1995') 
                --> : """)
                        if birthday:
                            patient.birthday = birthday

                        insurance = input("*** Enter patient's insurance or press 'Enter/Return' to keep current information: ")
                        if insurance:
                            patient.insurance = insurance

                        list_treatments()
                        print()
                        treatment_id = input("""*** Enter number from treatment list above or 
                    press 'Enter/Return' to keep current information: 
                        --> : """)
                        if treatment_id:
                            treatment_id = int(treatment_id)
                            patient.treatment_id = treatment_id

                        patient.update_patient()
                        new_treatment = Treatment.all.get(patient.treatment_id, None)
                        print()
                        print(f"Patient updated! --> Name: {patient.name}, DOB: {patient.birthday}, Insurance: {patient.insurance}, undergoing {new_treatment.name} treatment")

                    except Exception as exc:
                        print("Error updating patient, please try again:", exc)
    
            else: print("Invalid selection. Please try again.")
        
    except ValueError:
        print('Invalid input. Please enter a number')

def delete_patient():
    patients = list_patients()
    print()
    selected_patient = input("*** Enter the number of the patient you would like to delete:")
    print()
    try:
        selected_index = int(selected_patient) - 1
        if selected_index >= 0 and selected_index < len(patients):
            patient = patients[selected_index]
            patient.delete_patient_from_db()
            print()
            print(f"Patient {patient.name} deleted")

            remaining_pts = Patient.get_all_patients()

            for index, patient in enumerate(remaining_pts, start=1):
                patient.id = index
                patient.update_patient()

        else: print('Invalid selection. Please enter number corresponding to patient.')

    except ValueError: print('Invalid input. Please try again.')
    # patient = patients[int(selected_patient) - 1]
    # #if patient:
    # patient.delete_patient_from_db()
    # print()
    # print(f"Patient deleted")

    # remaining_pts = Patient.get_all_patients()

    # for index, patient in enumerate(remaining_pts, start=1):
    #     patient.id = index
    #     patient.update_patient()


#######


def list_treatments():
    treatments = Treatment.get_all_treatments()
    for i, treatment in enumerate(treatments, start=1):
        print()
        print(f'{i}. {treatment.name} for {treatment.duration} weeks')
    return treatments

def find_treatment_by_name():
    name = input("*** Enter name of treatment option (treatments are case-sensitive): ")
    treatment = Treatment.find_treatment_by_name(name)

    print(f'{treatment.name} for {treatment.duration} weeks') if treatment else print (f'Treatment named {name} not found')

def create_treatment():
    name = input("*** Enter treatment name: ")
    print()
    duration = input("""
*** Enter duration of treatment in weeks 
(For example, 3 months = 12 weeks; so enter 12):""")
    duration = int(duration)

    try:
        treatment = Treatment.create_treatment(name, duration)
        print()
        print(f'Sucessfully created new treatment! --> {treatment.name} for {treatment.duration} weeks')

    except Exception as exc:
        print(f'Error creating treatment, please start again:', exc)

def update_treatment_information():
    treatments = list_treatments()
    print()
    selected_treatment = input("*** Enter the number above corresponding to the treatment to update: ")

    try:
            selected_index = int(selected_treatment) - 1
            if selected_index >= 0 and selected_index < len(treatments):
                treatment = treatments[selected_index]
                if treatment:
                    print(f"""
            Treatment chosen --> {treatment.name} for {treatment.duration} weeks
                        """)
                    name = input("*** Enter a new name for the treatment or press 'Enter/Return' to keep current information: ")
                    if name:
                        treatment.name = name

                    duration = input("""*** Enter new duration of treatment in weeks 
            (For example, 3 months = 12 weeks; so enter 12) 
            or press 'Enter/Return' to keep current information
                --> : """)
                    if duration:
                        duration = int(duration) 
                        treatment.duration = duration

                    treatment.update_treatment()
                    print(f"""
        ***Treatment successfully updated! --> {treatment.name} for {treatment.duration} weeks""")
                    
            else: print("Invalid number. Please select number associated with treatment.")

    except Exception as exc:
            print("Error updating treatment, please try again:", exc)
    
def delete_treatment():
    treatments = list_treatments()

    selected_treatment = input("""
                    
*** To delete treatment, enter corresponding number for treatment above:
    
    --> : """)
    print()
    try:
        selected_index = int(selected_treatment) - 1
        if selected_index >= 0 and selected_index < len(treatments):
            treatment = treatments[selected_index]
            if not treatment:
                print(f"Treatment not found")
                return 
        
            patients = treatment.patients()

            treatment.delete_treatment_from_db()
            print(f"*** {treatment.name} treatment deleted")

            if patients:
                for patient in patients:
                    patient.treatment_id = None
                    patient.update_patient()
        
        else: print('Invalid Number. Please select number associated with treatment.')
    
    except ValueError: print('Invalid Selection. Please try again.')

def list_patients_in_treatment():
        treatments = list_treatments()

        selected_treatment = input("""
    *** To view patients, enter number of desired treatment above,
            and press 'Enter/Return': 
                         
            --> : """)
        
        try:
            selected_index = int(selected_treatment) - 1
            if selected_index >= 0 and selected_index < len(treatments):
                treatment = treatments[selected_index]
                patients = treatment.patients()
                if len(patients) > 0:
                        for i, patient in enumerate(patients, start=1):
                            print()
                            print(f'{i}. Name: {patient.name}, DOB: {patient.birthday}, Insurance: {patient.insurance}, undergoing {treatment.name} treatment')
                   
                else: 
                    print("No patients undergoing this treatment at this time")
            else: 
                print('Invalid Selection. Please select number corresponding to treatment.')
        
        except ValueError: print('Invalid Selection. Please try again')
        
            
def exit_program():
    print("""
          
          Exiting program...Goodbye!
          
          """)
    exit()


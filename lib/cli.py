# lib/cli.py

from helpers import (
    exit_program,
    list_patients,
    find_patient_by_name,
    create_patient,
    update_patient_information,
    delete_patient,
    list_treatments,
    find_treatment_by_name,
    create_treatment,
    update_treatment_information,
    delete_treatment,
    list_patients_in_treatment
)


def main():
    while True:
        menu()
        choice = input("Type number and press 'Enter/Return' to execute command --> ")
        if choice == "0":
            exit_program()

        elif choice == "1":
            while True:
                patient_menu()
                choice = input("Type number and press 'Enter/Return' to execute command --> ")
                if choice == "3":
                    list_patients()
                elif choice == "4":
                    find_patient_by_name()
                elif choice == "5":
                    create_patient()
                elif choice == "6":
                    update_patient_information()
                elif choice == "7":
                    delete_patient()
                elif choice == "0":
                    main()
                else: print ("Invalid choice --> Type '0' to exit program")

        elif choice == "2":
            while True:
                treatment_menu()
                choice = input("Type number and press 'Enter/Return' to execute command --> ")
                if choice == "8":
                    list_treatments()
                elif choice == "9":
                    find_treatment_by_name()
                elif choice == "10":
                    create_treatment()
                elif choice == "11":
                    update_treatment_information()
                elif choice == "12":
                    delete_treatment()
                elif choice == "13":
                    list_patients_in_treatment()
                elif choice == "0":
                    main()
                else: print ("Invalid choice --> Type '0' to exit program")

        else:
            print("Invalid choice")


def menu():
    print("""
          *** Welcome to the MD Database CLI interface! ***
          

    Please select from an option below and hit 'Enter/Return':

    --> Type '1' to list all the options for patients in database
    --> Type '2' to list all the options for treatments in database
    --> Type '0' to exit the program
          """)

def patient_menu():
    print()
    print("""
    *** Below are the options for patients in the database: ***

--> Type '3' to list all the patients in database
--> Type '4' to search for a patient by name in database
--> Type '5' to create a patient to add to database
--> Type '6' to update a patient's information in database
--> Type '7' to delete a patient in database
          
--> Type '0' to return to main menu
          """)

def treatment_menu():
    print()
    print("""
    *** Below are the options for treatments in the database: ***
          
    --> Type '8' to list all the treatments in database
    --> Type '9' to search for a treatment by name in database
    --> Type '10' to create a treatment to add to database
    --> Type '11' to update a treatment's information in database
    --> Type '12' to delete a treatment in database
    --> Type '13' to list all patients undergoing a particular treatment
          
    --> Type '0' to return to main menu
          """)

if __name__ == "__main__":
    main()


       
            

    

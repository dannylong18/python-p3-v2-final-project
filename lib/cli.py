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
        choice = input(">> ")
        if choice == "0":
            exit_program()
        elif choice == "1":
            helper_1()
        else:
            print("Invalid choice")


def menu():
    print("Please select an option:")
    print("0. Exit the program")
    print("1. Create patient")


if __name__ == "__main__":
    main()


       
            

    

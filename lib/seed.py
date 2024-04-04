#!/usr/bin/env python3

from models.__init__ import CONN, CURSOR
from models.patient import Patient
from models.treatment import Treatment

def seed_database():
    Patient.drop_table()
    Treatment.drop_table()

    Patient.create_table()
    Treatment.create_table()

    physical_therapy = Treatment.create_treatment('physical therapy', 6)
    pain_management = Treatment.create_treatment('pain management', 12)
    surgery = Treatment.create_treatment('surgery', 52)

    Patient.create_patient('John Doe', '12/18/1991', 'blue cross', physical_therapy.id)
    Patient.create_patient('Jane Buck', '10/03/1980', 'united', pain_management.id)
    Patient.create_patient('Justin Fawn', '05/22/1986', 'cigna', surgery.id)
    Patient.create_patient('Jordan Deer', '07/22/1945', 'medicare', surgery.id)

seed_database()
print("Database Seeded!")



#!/usr/bin/env python3

from models.__init__ import CONN, CURSOR
from models.patient import Patient
from models.treatment import Treatment

def seed_database():
    Patient.drop_table()
    Treatment.drop_table()

    Patient.create_table()
    Treatment.create_table()

    physical_therapy = Treatment.create_treatment('Physical Therapy', 6)
    pain_management = Treatment.create_treatment('Pain Management', 12)
    surgery = Treatment.create_treatment('Surgery', 52)

    Patient.create_patient('John Doe', 12181991, 'Blue Cross', physical_therapy.id)
    Patient.create_patient('Jane Buck', 1031980, 'United', pain_management.id)
    Patient.create_patient('Justin Fawn', 5221986, 'Cigna', surgery.id)
    Patient.create_patient('Jordan Deer', 7221945, 'Medicare', surgery.id)

seed_database()
print("Database Seeded!")



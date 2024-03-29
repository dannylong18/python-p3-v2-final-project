from models import CONN, CURSOR

class Patient:

    def __init__(self, name, birthday, insurance, treatment_id, id = None):
        self.id = id
        self.name = name
        self.birthday = birthday
        self.insurance = insurance
        self.treatment_id = treatment_id

    def __repr__(self):
        return f"<Patient {self.id}: {self.name}, {self.birthday}, {self.insurance}>"
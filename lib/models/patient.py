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
    
    @property
    def name (self):
        return self._name 
    
    @name.setter
    def name (self, name):
        if isinstance (name, str) and len(name):
            self._name = name
        
        else:
            raise ValueError ('Name must be a non-empty string')
        
    @property
    def birthday (self):
        return self._birthday
    
    @birthday.setter
    def birthday (self, birthday):
        if isinstance (birthday, int) and len(birthday):
            self._birthday = birthday

        else: 
            raise ValueError ('birthday must be an integer')
        
    @property
    
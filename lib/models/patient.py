from models import CONN, CURSOR
from models.treatment import Treatment

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
            raise ValueError ('birthday must be an appropriate integer')
        
    @property
    def insurance (self):
        return self._insurance
    
    @insurance.setter
    def insurance (self, insurance):
        if isinstance (insurance, str) and len(insurance):
            self._insurance = insurance

        else:
            raise ValueError ('Insurance must be a non-empty string')
    
    @property
    def treatment_id (self):
        return self._treatment_id
    
    @treatment_id.setter
    def treatment_id (self, treatment_id):
        if type(treatment_id) is int and Treatment.find_by_id(treatment_id):
            self._treatment_id = treatment_id
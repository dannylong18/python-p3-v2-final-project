from models import CONN, CURSOR

class Treatment:

    def __init__(self, name, date_started, id=None):
        self.id = id
        self.name = name
        self.date_started = date_started

    def __repr__(self):
        return f"<Treatment {self.id}: {self.name}, {self.date_started}>"
    
    @property
    def name (self):
        return self._name 
    
    @name.setter
    def name (self, name):
        if isinstance (name, str) and len(name):
            self._name = name
        
        else:
            raise ValueError ('Name must be a non-empty string')
        
    
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
        
    @property
    def date_started (self):
        return self._date_started 
    
    @date_started.setter
    def date_started (self, date_started):
        if isinstance (date_started, int) and len(date_started):
            self._date_started = date_started

        else:
            raise ValueError ('Date_started must be an appropriate integer')
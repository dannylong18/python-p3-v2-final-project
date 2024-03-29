from models import CONN, CURSOR

class Treatment:

    def __init__(self, name, date_started, id=None):
        self.id = id
        self.name = name
        self.dated_started = date_started

    def __repr__(self):
        return f"<Treatment {self.id}: {self.name}, {self.dated_started}>"
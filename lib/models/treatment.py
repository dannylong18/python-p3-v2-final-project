from models import CONN, CURSOR

class Treatment:

    all = {}

    def __init__(self, name, duration, id=None):
        self.id = id
        self.name = name
        self.duration = duration

    def __repr__(self):
        return f"Treatment {self.id} is {self.name} for {self.duration} weeks "
    
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
    def duration (self):
        return self._duration 
    
    @duration.setter
    def duration (self, duration):
        if isinstance (duration, int):
            self._duration = duration

        else:
            raise ValueError ('Duration must be an appropriate integer')
        
    
#######


    @classmethod
    def create_table(cls):
        sql = '''CREATE TABLE IF NOT EXISTS treatments (
        id INTEGER PRIMARY KEY, 
        name TEXT, 
        duration INTEGER)
        '''

        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        sql = '''DROP TABLE IF EXISTS treatments'''
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def create_treatment(cls, name, duration):
        treatment = cls(name, duration)

        treatment.save_treatment()

        return treatment
    
    @classmethod
    def treatment_from_db(cls, row):
        treatment = cls.all.get(row[0])
        
        if treatment:
            treatment.name = row[1]
            treatment.duration = row[2]

        else:
            treatment = cls(row[1], row[2])
            treatment.id = row[0]
            cls.all[treatment.id] = treatment

        return treatment 
    
    @classmethod
    def get_all_treatments(cls):
        sql = '''SELECT * FROM treatments'''

        treatments = CURSOR.execute(sql).fetchall()

        return [cls.treatment_from_db(row) for row in treatments]
    
    @classmethod
    def find_treatment_by_name (cls, name):
        sql = '''SELECT * FROM treatments WHERE name = ?'''

        treatment = CURSOR.execute(sql, (name,)).fetchone()

        return cls.treatment_from_db(treatment) if treatment else None
    
    @classmethod
    def find_treatment_by_id (cls, id):
        sql = '''SELECT * FROM treatments WHERE id = ?'''

        treatment = CURSOR.execute(sql, (id,)).fetchone()

        return cls.treatment_from_db(treatment) if treatment else None


#######


    def save_treatment(self):
        sql = '''INSERT INTO treatments (name, duration)
        VALUES (?, ?)'''

        CURSOR.execute(sql, (self.name, self.duration))
        CONN.commit()

        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self

    def update_treatment(self):
        sql = '''UPDATE treatments
                SET name = ?, duration = ?
                WHERE id = ?'''
        
        CURSOR.execute(sql, (self.name, self.duration))
        CONN.commit()

    def delete_treatment(self):
        sql = '''DELETE FROM treatments
                WHERE id = ?'''
        
        CURSOR.execute(sql, (self.id,))
        CONN.commit()

        del type(self).all[self.id]

        self.id = None

    def patients(self):
        from models.patient import Patient
        sql = '''SELECT * FROM patients
                WHERE treatment_id = ?'''
        
        CURSOR.execute(sql, (self.id,),)

        patients = CURSOR.fetchall()

        return [Patient.patient_from_db(patient) for patient in patients]
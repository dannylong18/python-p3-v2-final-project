from models import CONN, CURSOR
from models.treatment import Treatment

class Patient:

    all = {}

    def __init__(self, name, birthday, insurance, treatment_id, id = None):
        self.id = id
        self.name = name
        self.birthday = birthday
        self.insurance = insurance
        self.treatment_id = treatment_id

    def __repr__(self):
        return f"""{self.id}. Name: {self.name}, DOB:{self.birthday}, Insurance:{self.insurance} 
                """
    
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
        if isinstance (birthday, str) and len(birthday):
            self._birthday = birthday

        else: 
            raise ValueError ('birthday must be an non-empty string')
        
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
        if type(treatment_id) is int and Treatment.find_treatment_by_id(treatment_id):
            self._treatment_id = treatment_id

        else:
            raise ValueError ('Treatment_id must be appropriate integer')


#######


    @classmethod
    def create_table(cls):
        sql = '''CREATE TABLE IF NOT EXISTS patients (
        id INTEGER PRIMARY KEY, 
        name TEXT, 
        birthday TEXT, 
        insurance TEXT,
        treatment_id INTEGER,
        FOREIGN KEY (treatment_id) REFERENCES treatments(id))
        '''

        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        sql = '''DROP TABLE IF EXISTS patients'''
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def create_patient(cls, name, birthday, insurance, treatment_id):
        patient = cls(name, birthday, insurance, treatment_id)
        patient.save_patient()
        return patient 
    
    @classmethod
    def patient_from_db(cls, row):
        patient = cls.all.get(row[0])
        if patient:
            patient.name = row[1]
            patient.birthday = row[2]
            patient.insurance = row[3]
            patient.treatment_id = row[4]
        else:
            patient = cls(row[1], row[2], row[3], row[4])
            patient.id = row[0]
            cls.all[patient.id] = patient
        return patient 
    
    @classmethod
    def get_all_patients(cls):
        sql = '''SELECT * FROM patients'''

        patients = CURSOR.execute(sql).fetchall()

        return [cls.patient_from_db(row) for row in patients]
    
    @classmethod
    def find_patient_by_name (cls, name):
        sql = '''SELECT * FROM patients WHERE name = ?'''

        patient = CURSOR.execute(sql, (name,)).fetchone()
        return cls.patient_from_db(patient) if patient else None


#######


    def save_patient(self):
        sql = '''INSERT INTO patients (name, birthday, insurance, treatment_id)
        VALUES (?, ?, ?, ?)'''

        CURSOR.execute(sql, (self.name, self.birthday, self.insurance, self.treatment_id))
        CONN.commit()

        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self

    def update_patient(self):
        sql = '''UPDATE patients
                SET name = ?, birthday = ?, insurance = ?, treatment_id = ?
                WHERE id = ?'''
        
        CURSOR.execute(sql, (self.name, self.birthday, self.insurance, self.treatment_id, self.id))
        CONN.commit()

    def delete_patient(self):
        sql = '''DELETE FROM patients
                WHERE id = ?'''
        
        CURSOR.execute(sql, (self.id,))
        CONN.commit()

        del type(self).all[self.id]

        self.id = None
    

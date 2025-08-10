from app import db 

class Person(db.Model): 
    __tablename__ = 'people'
    
    pid = db.Column(db.Intger , primary_key=True)
    name = db.Column(db.text, nullable=False)
    age = db.Column(db.Intger)
    job = db.Column(db.text)
    
    def __repr__(self): 
        return f'name is {self.name} and age is {self.age} and job is {self.age}'
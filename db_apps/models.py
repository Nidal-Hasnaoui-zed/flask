from app import db

class Person(db.Model):
    __tablename__ = 'people'  # table name in DB

    pid = db.Column(db.Integer, primary_key=True)  # Primary key column
    name = db.Column(db.String(100), nullable=False)  # Name is required
    age = db.Column(db.Integer)
    job = db.Column(db.String(100))

    def __repr__(self):
        return f"<Person id={self.pid} name='{self.name}' age={self.age} job='{self.job}'>"

from flask_login import UserMixin

from app import db

# class Person(db.Model):
#     __tablename__ = 'people'

#     pid = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(100), nullable=False)
#     age = db.Column(db.Integer)
#     job = db.Column(db.String(100))

#     def __repr__(self):
#         return f"<Person id={self.pid} name={self.name!r} age={self.age} job={self.job!r}>"

class User(db.Model, UserMixin):
    __tablename__ = 'users'

    uid = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, nullable=False)
    password = db.Column(db.String, nullable=False)
    role = db.Column(db.String)
    description = db.Column(db.String)

    def __repr__(self):
        return f'<User: {self.username}, Role: {self.role}>'

    def get_id(self):
        return self.uid

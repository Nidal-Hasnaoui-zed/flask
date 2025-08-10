from flask import render_template, request
from models import Person
from app import db

def register_routes(app):

    @app.route('/')
    def index():
        people = Person.query.all()  # Get all people from DB
        return render_template('index.html', people=people)

    @app.route('/add', methods=['POST'])
    def add_person():
        name = request.form.get('name')
        age = request.form.get('age')
        job = request.form.get('job')

        if not name:
            return "Name is required!", 400

        person = Person(name=name, age=int(age) if age else None, job=job)
        db.session.add(person)
        db.session.commit()

        return f"Added {person.name} successfully!"

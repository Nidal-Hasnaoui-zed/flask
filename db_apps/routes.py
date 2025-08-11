from flask import render_template, request
from models import Person
from app import db  # import db only when needed (safe here)

def register_routes(app):
    @app.route('/')
    def index():
        people = Person.query.all()
        # quick plain text response (you can replace with render_template later)
        if not people:
            return "No people in DB yet"
        return render_template('index.html' , people=people)



    # this is advenced level bro !

    # @app.route('/add', methods=['POST'])
    # def add_person():
    #     name = request.form.get('name')
    #     age = request.form.get('age')
    #     job = request.form.get('job')
    #     if not name:
    #         return "Name required", 400
    #     p = Person(name=name, age=int(age) if age else None, job=job)
    #     db.session.add(p)
    #     db.session.commit()
    #     return f"Added {p.name}"

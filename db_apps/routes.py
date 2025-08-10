from flask import render_template , request
from models import Person 
from app import db  


def  register_routes(app): 
    @app.route('/')
    def index(): 
        people = Person.query.all()
        
        if not people : 
            return 'No data fond !' 
        
        return '<br>'.join([repr(p) for p in people]) 

    @app.route('/add', methods=['POST'])
    def add_person(): 
        name = request.form.get('name')
        age = request.form.get('age')
        job = request.form.get('job')
        
        if not name : 
            return 'name is nessecary !', 400  
        
        p = Person(name=name  , age=age if not age else None , job=job)
        db.session.add(p) 
        db.commit(p)
        
        return f'Added {name} into db !'      
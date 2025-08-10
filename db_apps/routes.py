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


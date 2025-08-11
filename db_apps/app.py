from flask import Flask 
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate 

db = SQLAlchemy()

def create_app(): 
    app = Flask(__name__, template_folder='templates')
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///testdb.db'
    
    db.init_app(app)
    Migrate(app , db)
    
    # after you create the route file imprte hem here !
    from routes import  register_routes
    register_routes(app)
    
    return app  

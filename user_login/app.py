from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_bcrypt import Bcrypt

db = SQLAlchemy()

def create_app():
    app = Flask(__name__, template_folder='templates')
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost/login_db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    app.secret_key = 'nidal'

    db.init_app(app)
    
    login_manager = LoginManager() 
    login_manager.init_app(app)
    
    from models import User
    
    @login_manager.user_loader
    
    def log_user(uid):
        return  User.query.get(uid)
        
        
    bcrypt = Bcrypt(app)

    # Import routes after db is defined to avoid circular import issues
    from routes import register_routes
    register_routes(app, db , bcrypt)
    
    migrate = Migrate(app, db)

    return app

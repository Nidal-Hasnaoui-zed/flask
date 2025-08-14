from flask import render_template, request
from models import User
from app import db  # import db only when needed (safe here)
from flask_login import login_user, logout_user, current_user , login_required

def register_routes(app, db , bcrypt ):
    @app.route('/')
    def index():
        if current_user.is_authenticated : 
            return str(current_user.username)
        else : 
            return 'No user is logged in '
   
   
    @app.route('/login/<uid>')
    def login(uid):
        user = User.query.get(uid)
        login_user(user)
        return 'Success !'
    
    @app.route('/logout')
    def logout():
        logout_user()
        return 'Success !'
from flask import render_template, request, redirect ,url_for
from models import User
from app import db  # import db only when needed (safe here)
from flask_login import login_user, logout_user, current_user , login_required

def register_routes(app, db , bcrypt ):
    @app.route('/')
    def index():
        render_template('index.html')
        
    @app.route('/signup', methods=['GET', 'POST'])  
    def signup(): 
        if request.method == 'GET'  : 
            return render_template('signup.html')
        elif request.method == 'POST' : 
            username = request.form.get('username')
            password = request.form.get('password')
            # we will hash the password : 
            hashed_password = bcrypt.generate_password_hash(password)
            
            user = User(username=username , password=hashed_password)     
            
            db.session.add(user)
            db.sesion.commit()   
            
            return redirect(url_for('index'))
            
            
    @app.route('/login', methods=['GET', 'POST'])  
    def login(): 
        if request.method == 'GET'  : 
            return render_template('login.html')
        elif request.method == 'POST' : 
            username = request.form.get('username')
            password = request.form.get('password')
            user = User.query.filter(User.username == username).first()

            if bcrypt.check_password_hash(user.password, password):
                login_user(user)
                return render_template('index.html')
            else:
                return 'Failed'
   
    @app.route('/login/<uid>')
    def login(uid):
        user = User.query.get(uid)
        login_user(user)
        return 'Success !'
    
    @app.route('/logout')
    def logout():
        logout_user()
        return 'Success !'
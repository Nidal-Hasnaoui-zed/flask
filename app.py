from flask import Flask , render_template , session, make_response

app = Flask(__name__ , template_folder='templates')

app.secret_key = 'nidal'

@app.route('/')
def index(): 
    return render_template('index.html', message='this is the index page !')

# we will set an session !
@app.route('/set_data')
def set_data(): 
    session['username'] = 'nidal'
    session['job'] = 'backend'
    return render_template('index.html', message='this is how  you can set data in session !')


#lets get a data from a session !
@app.route('/get_data')
def get_data() : 
    if 'usernmae' in session.keys() and 'job' in session.keys() : 
        username = session['usename']
        job = session['job']
        return render_template('index.html', mesage=f'the user name is {username} and job is {job}')
    else : 
        return render_template('index.html', message='no session found !')
    
#clear session !
@app.route('/clear_session')
def session_clear() : 
    session.clear()
    render_template('index.html', message='all session was cleard !')

#set a coookie !
@app.route('/set_cookie ')
def set_cookie(): 
    response = make_response(render_template('index.html', message='creating a cookie'))
    response.set_cookie('Cookie_name', 'Cookie_value'); 
    return response
   
   
   
if __name__ == '__main__': 
    app.run(debug=True)
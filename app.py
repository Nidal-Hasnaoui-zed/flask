from flask import Flask , render_template , session , make_response

app = Flask(__name__ ,template_folder='templates')
# main func !
@app.route('/')
def index():
    return render_template('index.html', message='index')

#set data func !
@app.route('/set_data')
def set_data(): 
    session['username'] = 'nidal'
    session['job'] = 'backend'
    return render_template('index.html', message='Session data Set !')

#get data func !
@app.route('/get_data')
def get_data(): 
    if 'username' in session.keys() and 'job' in session.keys() :
        username = session['usename']
        job = session['job']
        return render_template('index.html', message=f'the user name is {username} and job is {job}')
    else : 
        return render_template('index.html', message='No session found !')
        
#clear session func !    
@app.route('/clear_session')
def clear_session(): 
    session.clear()
    return render_template('index.html',message='Session cleared.')    
#make app run !
if __name__ == '__main__'  : 
    app.run(debug=True)
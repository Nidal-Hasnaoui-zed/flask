from flask import Flask, render_template, session, make_response, request, flash

app = Flask(__name__, template_folder='templates')
app.secret_key = 'nidal'  # ضروري للـ session و flash

# صفحة البداية
@app.route('/')
def index(): 
    return render_template('index.html', message='This is the index page!')

# حفظ بيانات في الـ session
@app.route('/set_data')
def set_data(): 
    session['username'] = 'nidal'
    session['job'] = 'backend'
    return render_template('index.html', message='Data has been set in session!')

# جلب البيانات من الـ session
@app.route('/get_data')
def get_data(): 
    if 'username' in session and 'job' in session: 
        username = session['username']
        job = session['job']
        return render_template('index.html', message=f'The user name is {username} and job is {job}')
    else: 
        return render_template('index.html', message='No session found!')

# مسح الـ session
@app.route('/clear_session')
def session_clear(): 
    session.clear()
    return render_template('index.html', message='All session data was cleared!')

# إنشاء كوكي
@app.route('/set_cookie')
def set_cookie(): 
    response = make_response(render_template('index.html', message='Cookie created!'))
    response.set_cookie('cookie_name', 'cookie_value')
    return response

# جلب الكوكي
@app.route('/get_cookie')
def get_cookie(): 
    cookie_value = request.cookies.get('cookie_name')
    if cookie_value:
        return render_template('index.html', message=f'The cookie value is: {cookie_value}')
    else:
        return render_template('index.html', message='No cookie found.')

# إزالة الكوكي
@app.route('/remove_cookie')
def remove_cookie():
    response = make_response(render_template('index.html', message='Cookie removed.'))
    response.set_cookie('cookie_name', '', expires=0)
    return response

# صفحة تسجيل الدخول
@app.route('/login', methods=['GET', 'POST'])
def login(): 
    if request.method == 'GET': 
        return render_template('index.html')
    elif request.method == 'POST': 
        username = request.form.get('username')
        password = request.form.get('password')
        if username == 'nidal' and password == 'nidal': 
            flash('Successful login!')
        else: 
            flash('Login failed!')
        return render_template('index.html')

if __name__ == '__main__': 
    app.run(debug=True)

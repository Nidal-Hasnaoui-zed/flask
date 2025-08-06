from flask import Flask , render_template , session , make_response

app = Flask(__name__ ,template_folder='templates')

@app.route('/')
def index():
    return render_template('index.html', message='index')


@app.route('/set_data')
def set_data(): 
    session['username'] = 'nidal'
    session['job'] = 'backend'
    return render_template('index.html', message='Session data Set !')


 
if __name__ == '__main__'  : 
    app.run(debug=True)
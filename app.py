from flask import Flask , render_template, redirect , url_for

app = Flask(__name__,template_folder='templates')

@app.route('/')
def Hey(): 
    return render_template('index.html')


#dynmic valirables : 
@app.route('/index1')
def index1(): 
    name = 'nidal'
    lname = 'hasnaoui'
    age = 19 
    job = 'backend'
    langs = ['js','php','pyhton','sql']
    return render_template('index1.html', name=name , lname=lname, age=age, job=job,langs=langs)
    
@app.route('/other')
def other(): 
    some_text = 'nidal'
    return render_template('other.html' , some_text=some_text)

@app.template_filter('revise')
def revise(s): 
    return s[::-1]
#rediretcion 
@app.route('/redirection')
def redir(): 
    return redirect(url_for('index1'))
if __name__ == '__main__': 
    app.run(debug=True)
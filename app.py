from flask import Flask , render_template , redirect , url_for

app = Flask(__name__, template_folder='templates')

@app.route('/test')
def index2(): 
    return render_template('index.html')

@app.route('/')
def index1(): 
    name = 'nidal'
    age = 19 
    dream_job = 'backend Dev'
    my_langs = ['html','css','js','php','python']
    return render_template('index1.html', name=name, age=age, dream_job=dream_job,my_langs=my_langs)

#filters : 
@app.route('/other')
def other(): 
    some_text = 'nidal '
    return render_template('other.html', some_text=some_text)

# lets create our filters here 
@app.template_filter('revise_string')
def revise_string(s): 
    return s[::-1]
# lets ceate other filter !
@app.template_filter('reapete')
def reapete(s,times=2): 
    return s * times

# a function for redirect for !
@app.route('/redirect_endpoint')
def redirect_endpoint(): 
    return redirect(url_for('other'))

if __name__ == '__main__' : 
    app.run(debug=True)
    
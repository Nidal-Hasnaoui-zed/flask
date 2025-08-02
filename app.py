from flask import Flask , render_template

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
    

if __name__ == '__main__': 
    app.run(debug=True)
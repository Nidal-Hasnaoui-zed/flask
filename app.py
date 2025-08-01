from flask import Flask , render_template 

app = Flask(__name__, template_folder='templates')

@app.route('/')
def testing(): 
    name = 'nidal'
    age = 19 
    dream_job = 'backend Dev'
    return render_template('index.html', name=name, age=age, dream_job=dream_job)

if __name__ == '__main__' : 
    app.run(debug=True)
    
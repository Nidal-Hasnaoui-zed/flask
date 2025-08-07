from flask import Flask , render_template 

app = Flask(__name__ , template_folder='templates')

app.secret_key = 'nidal'

@app.route('/')
def index(): 
    return render_template('index.html', message='this is the html page !')

if __name__ == '__main__': 
    app.run(debug=True)
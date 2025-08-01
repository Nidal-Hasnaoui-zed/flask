from flask import Flask 

app = Flask(__name__)

@app.route('/')
def home_page(): 
    return 'this is the home page bro !'

# adding html !
@app.route('/add_html')
def add_html():
    return '<h1>Hey this is me again nidal</h1>'

# add dynamic url ! 
@app.route('/greating/<name>')
def greating(name):
    return f'Welcome in our Website {name}'

if __name__ == '__main__': 
    app.run(debug=True)
from flask import Flask , request

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

# add a math function : 
@app.route('/math/<int:num1>/<int:num2>')
def get_sum(num1,num2):
    return f'the sum is {num1 + num2}' 

# lets handle paramets bro ! :
@app.route('/handel_parms')
def handel_parms(): 
    return str(request.args)

if __name__ == '__main__': 
    app.run(debug=True)
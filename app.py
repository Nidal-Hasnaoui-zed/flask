from flask import Flask , request

app = Flask(__name__)

@app.route('/')
def say_hey(): 
    return 'hey my name is nidal hasnaoui !'

#adding other function in other url !
@app.route('/page2')
def page2(): 
    return '<h1>Welcome from page 2 !</h1>'

#here i will teach you dunamic urls bro !
@app.route('/greating/<name>')
def greating(name): 
    return f'Hello, {name}'

# lets try do some math functions : 
@app.route('/add/<int:num1>/<int:num2>')
def summ(num1, num2) : 
    return f'the sum is : {num1 + num2}'

#handle urls !
@app.route('/handle_params')
def handle(): 
    return str(request.args)

#handle urls 2 : 
@app.route('/handle_parms2')
def handle2(): 
    greating = request.args['greating']
    name = request.args.get('name')
    return f'{greating}, {name}'


if __name__ == '__main__' : 
    app.run()
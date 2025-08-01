from flask import Flask , request, make_response 

app = Flask(__name__)

# i understand this function !
@app.route('/')
def say_hey(): 
    return 'hey my name is nidal hasnaoui !'

#adding other function in other url ! (i got it !)
@app.route('/page2')
def page2(): 
    return '<h1>Welcome from page 2 !</h1>'

#here i will teach you dunamic urls bro ! (i got it !)
@app.route('/greating/<name>')
def greating(name): 
    return f'Hello, {name}'

# lets try do some math functions : (i got it !)
@app.route('/add/<int:num1>/<int:num2>')
def summ(num1, num2) : 
    return f'the sum is : {num1 + num2}'

#handle urls ! i understad but that in what will helps us ? 
@app.route('/handle_params')
def handle(): 
    return str(request.args)

#handle urls 2 : i understad but that in what will helps us ? 
@app.route('/handle_parms2')
def handle2(): 
    if 'greating' in request.args.keys() and 'name' in request.args.keys():
        greating = request.args['greating']
        name = request.args.get('name')
        return f'{greating}, {name}'
    else : 
        return 'Some params is messing !'
#methods : (i dont understand it bro !)
@app.route('/method_tets', methods=['GET','POST'])
def methods_test(): 
    if request.method == 'GET' : 
        return 'you use get Method !'
    else : 
        return 'you use post Method'
    
#lets try somthing i just see them : (i dont understand it bro !) in what 200 used for ? 
@app.route('/testing')
def testing(): 
    return 'hello world !' , 200    

#lets try somthing i just see them again about responce : (i dont understand it bro !)
@app.route('/responce')
def responce() : 
    responce = make_response()
    responce.status_code = 1212
    responce.headers['content-type'] = 'application/octet-stream'
    return responce

if __name__ == '__main__' : 
    app.run()
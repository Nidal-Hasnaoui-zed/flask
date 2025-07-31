from flask import Flask 

app = Flask(__name__)

@app.route('/')
def say_hey(): 
    return 'hey my name is nidal hasnaoui !'

#adding other function in other url !
@app.route('/page2')
def page2(): 
    return '<h1>Welcome from page 2 !</h1>'

if __name__ == '__main__' : 
    app.run()
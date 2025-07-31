from flask import Flask 

app = Flask(__name__)

@app.route('/')

def say_hey(): 
    return 'hey my name is nidal hasnaoui !'

if __name__ == '__main__' : 
    app.run()
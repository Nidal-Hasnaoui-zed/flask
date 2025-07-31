#importing flask class from Flask libary !
#why ? : for you can build an simple web app !
from flask import Flask 

# create an instance of flask class bro !
#why ? : bc if you run the file direclty , '__name__' will be '__main__'
app = Flask(__name__)

# this is the dirictor will link page (/) 'landing page' with hsi function !
# so ? : if you opend this link will run next function !
@app.route('/') 

# this is a simple function return my name !
def say_hey(): 
    return 'hey my name is nidal !'



#here you said if i run the app diriclty gives me reszult of this file !
if __name__ == '__main__' : 
    app.run()
    
# ask chat gpt for you can understad this one !
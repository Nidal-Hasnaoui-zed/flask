#importing flask class from Flask libary !
#why ? : for you can build an simple web app !
from flask import Flask 

# create an instance of flask class bro !
#why ? : bc if you run the file direclty , '__name__' will be '__main__'
app = Flask(__name__)

@app.route('/') 


# this is a simple function return my name !
def say_hey(): 
    return 'hey my name is nidal !'

# lets add some other page !
def job(): 
    return 'my job is back end Dev !'
app.add_url_rule('/job', 'job', job)   # and i dont understand this bro bc  just coppy it 

#and  i dont understand this ine bro !
if __name__ == '__main__' : 
    app.run()
    
# ask chat gpt for you can understad this one !
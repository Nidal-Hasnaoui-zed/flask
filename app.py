from flask import Flask # i dont understand what the meaning of this one !

app = Flask(__name__) # and this i dont understand it why we write it !

@app.route('/') # i have a simple idea this is the default url will show if you run the app !


# this is a simple function return my name !
def say_hey(): 
    return 'hey my name is nidal !'

#and  i dont understand this ine bro !
if __name__ == '__main__' : 
    app.run()
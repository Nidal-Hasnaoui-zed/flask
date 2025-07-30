from flask import Flask # i dont understand what the meaning of this one !

app = Flask(__name__) # and this i dont understand it why we write it !

@app.route('/') # i have a simple idea this is the default url will show if you run the app !


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
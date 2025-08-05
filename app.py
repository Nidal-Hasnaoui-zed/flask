from flask import Flask , template_rendered , request

app = Flask(__name__, template_folder='templates')

@app.rout('/', methods=['GET','POST'])
def index(): 
    if request.method == 'GET' : 
        return template_rendered('index.html')
    elif request.method == 'POST' : 
        user_name = request.form.get('username')
        password = request.form.get('pwd')
        
    if user_name == 'nidal' and password == 'nidal' : 
        return 'Weclome bro !'
    else : 
        return 'Try again password or user name is not valid !'
    

if __name__ == '__main__' : 
    app.run(debug=True)
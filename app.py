from flask import Flask , render_template , request

app = Flask(__name__, template_folder='templates')

@app.route('/', methods=['GET','POST'])
def index(): 
    if request.method == 'GET' : 
        return render_template('index.html')
    elif request.method == 'POST' : 
        username = request.form.get('username')
        pwd = request.form.get('pwd')
        
        if username == 'nidal' and pwd == 'nidal' : 
            return 'welcome !'
        else : 
            return 'Sorry Try Again !'
 
if __name__ == '__main__': 
    app.run(debug=True)
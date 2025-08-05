from flask import Flask , template_rendered , request

app = Flask(__name__, template_folder='templates')

@app.rout('/', methods=['GET','POST'])
def index(): 
    if request.method == 'GET' : 
        return template_rendered('index.html')
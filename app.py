from flask import Flask , template_rendered 

app = Flask(__name__, template_folder='templates', static_folder='static', static_url_path='/')

@app.route('/') 
def index() : 
    return template_rendered('index.html')

if __name__ == '__main__' : 
    app.run(debug=True) 
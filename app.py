from flask import Flask , render_template , session , make_response

app = Flask(__name__ ,template_folder='templates')

@app.route('/')
def index():
    return render_template('index.html', message='index')

 
if __name__ == '__main__'  : 
    app.run(debug=True)
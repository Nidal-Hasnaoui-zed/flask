from flask import Flask 
app = Flask(__name__)
@app.route('/')
def Hey(): 
    return 'hey !'
if __name__ == '__main__': 
    app.run(debug=True)
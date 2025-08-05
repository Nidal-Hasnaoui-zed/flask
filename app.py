from flask import Flask , template_rendered 

app = Flask(__name__, template_folder='templates', static_folder='static', static_url_path='/')


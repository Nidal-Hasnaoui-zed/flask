from flask import Flask , template_rendered , request

app = Flask(__name__, template_folder='templates')
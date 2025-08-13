from flask import render_template, request
from models import User
from app import db  # import db only when needed (safe here)

def register_routes(app):
    @app.route('/', methods=['GET', 'POST'])
    def index():
       return ""
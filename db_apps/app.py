from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# Create db object now (not connected to app yet)
db = SQLAlchemy()

def create_app():
    app = Flask(__name__, template_folder='templates')

    # Database configuration
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///testdb.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Avoid extra warnings

    # Connect db to this app
    db.init_app(app)

    # Enable database migrations
    Migrate(app, db)

    # Import routes AFTER db is ready to avoid circular import problems
    from routes import register_routes
    register_routes(app)

    return app

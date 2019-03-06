"""Main application and routing logic for Twitter Comp"""
from flask import Flask
from .models import DB


def create_app():
    """Create and configure an instance of the Flask application."""
    """config is basically a python dict"""
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    DB.init_app(app)

    @app.route('/')
    def root():
        return 'Welcome to TwitOff!'

    return app
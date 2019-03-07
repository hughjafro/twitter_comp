"""Main application and routing logic for Twitter Comp"""
from decouple import config
from flask import Flask, render_template, request
from .models import DB, User


def create_app():
    """Create and configure an instance of the Flask application."""
    """config is basically a python dict"""
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = config('DATABASE_URL')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    DB.init_app(app)

    @app.route('/')
    def root():
        users = User.query.all()
        return render_template('base.html', title='Home', users=users)

    @app.route('/reset')
    def reset():
        DB.drop_all()
        DB.create_all()
        return render_template('base.html', title='DB reset', users=[])

    return app
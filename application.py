from flask import Flask
from flask.ext import login

from models.base import db
from models.user import User
from config import Config

def init_login(app):
    login_manager = login.LoginManager()
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(user_id):
        return db.session.query(User).get(user_id)

def init_config(app):
    app.config.from_object(Config)

def create_app(name):
    app = Flask(name)
    
    init_config(app)
    db.init_app(app)
   
    init_login(app)
    return app

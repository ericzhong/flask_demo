import os
import logging


class Config(object):
    """
        Default configuration of application.
    """
    
    DEBUG = True

    # Create dummy secrey key so we can use sessions
    SECRET_KEY = '123456790'

    # Database
    SQLALCHEMY_DATABASE_URI = 'sqlite:///sample_db.sqlite'
    SQLALCHEMY_ECHO = True

# config.py

import os
from app import app
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.migrate import Migrate, MigrateCommand


basedir = os.path.abspath(os.path.dirname(__file__))

APP_DEBUG = True
CSRF_ENABLED = True

""" Database configuration """
try:
    from local_settings import *
except ImportError:
    pass

# Enables automatic commits to database changes at the end of each request
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True

SQLALCHEMY_TRACK_MODIFICATIONS = True

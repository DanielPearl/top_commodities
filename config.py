# config.py

import os
from app import app
from local_settings import *

basedir = os.path.abspath(os.path.dirname(__file__))

DEBUG = True
APP_DEBUG = True
CSRF_ENABLED = True

# Enables automatic commits to database changes at the end of each request
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True

SQLALCHEMY_TRACK_MODIFICATIONS = True

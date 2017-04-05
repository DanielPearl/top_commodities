# __init__.py

from flask import Flask

from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker


app = Flask(__name__)

# Config
app.config.from_object('config')

# SQL Alchemy
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# DB Migration
manager = Manager(app)
manager.add_command('db', MigrateCommand)

# Create Session
Session = sessionmaker()
engine = create_engine(app.config['SQLALCHEMY_DATABASE_URI'])
Session.configure(bind=engine)

from app import views, models

if __name__ == '__main__':
    manager.run()

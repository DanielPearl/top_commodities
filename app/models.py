# models.py

from flask import Flask
from app import app, db
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand


migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)

class CropAnnualProduction(db.Model):
    __tablename__ = 'crop_annual_production'
    id = db.Column(db.Integer, primary_key=True)
    Country = db.Column(db.String(255))
    Item = db.Column(db.String(255))
    Year = db.Column(db.Integer)
    Unit = db.Column(db.String(255), nullable=True)
    Value = db.Column(db.Float(255), nullable=True)


    # def __repr__(self):
    #     return "{0} {1} {2} {3} {4}".format(self.Country, self.Year, self.Item, round(float(self.Value),2), self.Unit)

if __name__ == '__main__':
    manager.run()

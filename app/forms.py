from app import app, models, db
from flask.ext.wtf import Form
from wtforms import StringField, SubmitField, SelectField, SelectMultipleField
from wtforms.validators import Required
from sqlalchemy.sql import text

connection = db.engine.connect()

# Country query
countries = connection.execute(text("SELECT DISTINCT Country, Country FROM crop_annual_production")).fetchall()
print(countries)
# Crop query
crops = connection.execute(text("SELECT DISTINCT Item, Item FROM crop_annual_production")).fetchall()

# Year query
years = connection.execute(text("SELECT DISTINCT Year, Year FROM crop_annual_production")).fetchall()

class NameForm(Form):
    country = SelectField('Country', choices=countries)
    crop = SelectField('Crop', choices=crops, validators = [Required()])
    year = SelectField('Year', choices=years, validators = [Required()])

    submit = SubmitField('Submit')

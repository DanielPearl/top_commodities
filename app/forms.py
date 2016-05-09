from app import app, models, db
from flask.ext.wtf import Form
from wtforms import StringField, SubmitField, SelectField, SelectMultipleField
from wtforms.validators import Required
from sqlalchemy.sql import text

connection = db.engine.connect()

# Country query
countries = connection.execute(text("SELECT DISTINCT Country FROM crop_annual_production")).fetchall()

# Crop query
crops = connection.execute(text("SELECT DISTINCT Item FROM crop_annual_production")).fetchall()

# Year query
years = connection.execute(text("SELECT DISTINCT Year FROM crop_annual_production")).fetchall()

print(years)

class NameForm(Form):
    country = SelectField('Country', choices=[("Australia","Australia"),("Algeria","Algeria")])
    crop = SelectField('Crop', choices=[("Wine","Wine"),("Molasses","Molasses"),("Cottonseed", "Cottonseed")], validators = [Required()])
    year = SelectField('Year', choices=[(2010,2010),(2011,2011)], validators = [Required()])

    submit = SubmitField('Submit')

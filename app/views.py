# views.py

from flask import render_template, flash, redirect
from app import app, models, db
import json
import plotly.plotly as py
import pandas as pd
from sqlalchemy.sql import text
from MapDataList2D import MapDataStructure

@app.route('/')
@app.route('/index')
def index():
    cap = models.CropAnnualProduction()
    user = {'first_name': 'Daniel'}
    connection = db.engine.connect()
    sql = "SELECT * FROM crop_annual_production WHERE Item LIKE '%{0}%' AND Year = '{1}' AND Country != 'World' AND Country NOT LIKE '%Americas%' AND Country != 'North America' AND Country != 'South America' AND Country != 'Central America' AND Country NOT LIKE '%Europe%' AND Country != 'Africa' AND Country != 'Western Africa' AND Country NOT LIKE '%Asia%' AND Country NOT LIKE '%Countries%'".format("Wine", 2010)
    results = connection.execute(text(sql)).fetchall()

    tdl = MapDataStructure(['Country', 'Value'])

    for i in range(len(results)):
        # access the result at i
        result = results[i]
        country = result.Country
        val = result.Value
        tdl.add_row([country, int(round(float(results[i].Value)))])

    lstats = tdl.generate_data()

    return render_template('index.html',
                           title='Home',
                           user=user,
                           posts=lstats)

#

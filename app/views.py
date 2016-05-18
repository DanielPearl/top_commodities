# views.py

from flask import render_template, flash, redirect, request
from app import app, models, db
import json
import plotly.plotly as py
import pandas as pd
from sqlalchemy.sql import text
from MapDataList2D import MapDataStructure
from app import forms


@app.route('/', methods=['GET', 'POST'])
def index():
    # Get items from form
    form = forms.NameForm()
    country, crop, year = None, None, None
    if request.method == 'POST':
        country = form.country.data
        crop = form.crop.data
        year = form.year.data

    # Map query
    connection = db.engine.connect()
    if country != "All":
        sql = "SELECT * FROM crop_annual_production WHERE Country = '{0}' AND Item = '{1}' AND Year = '{2}' AND Value != '{3}' AND Value > 0 AND Element ='Production' AND Country_Code < 1000".format(country, crop, year, None)
    else:
        sql = "SELECT * FROM crop_annual_production WHERE Item = '{0}' AND Year = '{1}' AND Value != '{2}' AND Value > 0 AND Element ='Production' AND Country_Code < 1000".format(crop, year, None)
    results = connection.execute(text(sql)).fetchall()

    tdl = MapDataStructure()

    for i in range(len(results)):
        # access the result at i
        result = results[i]
        country = result.Country
        val = result.Value
        tdl.add_row([country, results[i].Value])

    lstats = tdl.generate_js_list()
    lstats.sort(key=lambda x: x[1], reverse=True)
    lstats.insert(0,["Country","Tonnes"])

    return render_template('index.html',
                           title='Home',
                           form = form,
                           posts=lstats,
                           crop=crop,
                           country=country)

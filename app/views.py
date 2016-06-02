# views.py

from flask import render_template, flash, redirect, request
from app import app, models, db
import json
from sqlalchemy.sql import text
from MapDataList2D import MapDataStructure
from app import forms

def sql_query(country, crop, year):
    if country != "All" and crop != "All":
        return "SELECT * FROM crop_annual_production WHERE Country NOT LIKE '%,%' AND Country NOT LIKE '%(%' AND Country = '{0}' AND Item = '{1}' AND Year = '{2}' AND Value != '{3}' AND Value > 0 AND Element ='Production' AND Country_Code < 1000".format(country, crop, year, None)
    elif country != "All" and crop == 'All':
        return "SELECT * FROM crop_annual_production WHERE Country = '{0}' AND Country NOT LIKE '%,%' AND Country NOT LIKE '%(%' AND Value != '{1}' AND Value > 0 AND Year = '{2}' AND Element ='Production' AND Country_Code < 1000".format(country, None, year)
    else:
        return "SELECT * FROM crop_annual_production WHERE Country NOT LIKE '%,%' AND Country NOT LIKE '%(%' AND Item = '{0}' AND Year = '{1}' AND Value != '{2}' AND Value > 0 AND Element ='Production' AND Country_Code < 1000".format(crop, year, None)

@app.route('/', methods=['GET', 'POST'])
def index():
    # Get items from form
    form = forms.NameForm()
    country, crop, year = None, None, None
    if request.method == 'POST':
        country = form.country.data
        crop = form.crop.data
        year = form.year.data

    # sql query
    sql = sql_query(country, crop, year)

    # Map query
    connection = db.engine.connect()

    results = connection.execute(text(sql)).fetchall()
    print(results)
    tdl = MapDataStructure()

    if country != "All" and crop == "All":
        for i in range(len(results)):
            result = results[i]
            item = result.Item
            value = result.Value
            tdl.add_row([item, value])
    else:
        for i in range(len(results)):
            # access the result at i
            result = results[i]
            country = result.Country
            value = result.Value
            tdl.add_row([country, value])

    lstats = tdl.generate_js_list()
    lstats.sort(key=lambda x: x[1], reverse=True)
    lstats.insert(0,["Country","Tonnes"])

    return render_template('index.html',
                           title='Home',
                           form = form,
                           posts=lstats,
                           crop=crop,
                           country=country)

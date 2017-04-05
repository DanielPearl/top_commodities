# views.py

from flask import render_template, flash, redirect, request
from app import app, models, db
import json

from .models import *


@app.route("/", methods=["GET"])
def index():
    title = "Top Commodities"

    return render_template('index.html')

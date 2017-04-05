# models.py

from flask import Flask
from app import app, db

from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, ForeignKey


class Country(db.Model):
    __tablename__ = 'countries'
    id = Column(Integer, primary_key=True)
    country_code = Column(Integer)
    country_name = Column(String(255))

class Crop(db.Model):
    __tablename__ = 'crops'
    id = Column(Integer, primary_key=True)
    crop_code = Column(Integer)
    crop_name = Column(String(255))

class Element(db.Model):
    __tablename__ = 'elements'
    id = Column(Integer, primary_key=True)
    element_code = Column(Integer)
    element_name = Column(String(255))

class Unit(db.Model):
    __tablename__ = 'units'
    id = Column(Integer, primary_key=True)
    unit_code = Column(Integer)
    unit_name = Column(String(255))

class CropProduction(db.Model):
    __tablename__ = 'crops_production'
    id = Column(Integer, primary_key=True)
    country_code = Column(Integer, ForeignKey('countries.country_code'))
    crop_code = Column(Integer, ForeignKey('crops.crop_code'))
    element_code = Column(Integer, ForeignKey('elements.element_code'))
    year = Column(Integer)
    value = Column(Integer)

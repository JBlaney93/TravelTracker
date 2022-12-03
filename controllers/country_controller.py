from flask import Flask, render_template
from models.country import Country 
from repositories import country_repository

from app import app

@app.route("/countries")
def countries():
    countries = country_repository.select_all()
    return render_template("countries/index.html", countries=countries)
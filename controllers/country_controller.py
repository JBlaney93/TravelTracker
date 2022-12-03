from flask import Flask, render_template, request, redirect
from models.country import Country 
from repositories import country_repository

from app import app

@app.route('/countries')
def countries():
    countries = country_repository.select_all()
    return render_template('countries/index.html', countries=countries)


@app.route('/countries/new')
def new_country():
    return render_template('countries/new_country.html')


@app.route('/countries', methods=['POST'])
def save_country():
    visited = False
    form_data = request.form
    country_name = form_data['country_name']
    cities = form_data['cities']
    
    if 'visited' in form_data:  
        visited = True

    new_country = Country(country_name, cities, visited)
    country_repository.save(new_country)

    return redirect('/countries')
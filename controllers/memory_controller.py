from flask import Flask, render_template, request, redirect
from models.memory import Memory
from models.user import User
from models.country import Country
from repositories import memory_repository, user_repository, country_repository

from app import app

@app.route('/memories')
def memory():
    memories = memory_repository.select_all()
    return render_template('memories/index.html', memories=memories)


@app.route('/memories/new')
def new_memory():
    users = user_repository.select_all()
    countries = country_repository.select_all()
    return render_template('memories/new_memory.html', users=users, countries=countries)


@app.route('/memories', methods=['POST'])
def save_memory():
    form_data = request.form
    memory = form_data['memory']
    user_id = form_data['user_id']
    country_id = form_data['country_id']

    user = user_repository.select_user_by_id(user_id)
    country = country_repository.select_country_by_id(country_id)

    new_memory = Memory(user, country, memory)
    memory_repository.save(new_memory)

    return redirect('/memories')


@app.route('/memories/delete/<id>', methods=['POST'])
def delete_memory(id):
    memory_repository.delete(id)

    return redirect('/memories')

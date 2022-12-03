from flask import Flask, render_template, request, redirect
from models.user import User
from repositories import user_repository

from app import app

# EXAMPLES ARE USING BLUEPRINT BUT I DON'T KNOW HOW TO USE IT
# JAMMING APP.ROUTE IN PLACE INSTEAD

# RESTful CRUD Routes 

# INDEX
# GET '/users'

@app.route('/users') 
def users():
        users = user_repository.select_all()
        return render_template('users/index.html', users=users)


@app.route('/users/new')
def new_user():
        return render_template('users/new_user.html')


@app.route('/users', methods=['POST'])
def save_user():
        form_data = request.form
        name = form_data['user_name']

        new_user = User(name)
        user_repository.save(new_user)

        return redirect('/users')


@app.route('/users/delete/<id>', methods=['POST'])
def delete_user(id):
        user_repository.delete(id)

        return redirect('/users')

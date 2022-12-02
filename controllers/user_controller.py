from flask import Flask, render_template
from models.user import User
from app import app

# EXAMPLES ARE USING BLUEPRINT BUT I DON'T KNOW HOW TO USE IT
# JAMMING APP.ROUTE IN PLACE INSTEAD

# RESTful CRUD Routes 

# INDEX
# GET '/users'

@app.route("/users") 
def users():
        user = User('James')
        return render_template("users/index.html", users=[user])




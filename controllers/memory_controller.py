from flask import Flask, render_template
from models.memory import Memory
from repositories import memory_repository

from app import app

@app.route("/memories")
def memory():
    memories = memory_repository.select_all()
    return render_template("memories/index.html", memories=memories)
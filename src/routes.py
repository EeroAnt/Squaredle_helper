from app import app
from flask import render_template
from src.services.create_grid import create_grid

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/create_grid")
def create_grid():
    create_grid()
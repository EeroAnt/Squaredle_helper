from app import app
from flask import render_template
from src.services.create_grid import _get_grid_size

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/create_grid", methods=["POST"])
def create_grid():
    size = _get_grid_size()
    return render_template("submit_grid.html", size=size)
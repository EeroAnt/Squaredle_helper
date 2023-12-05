from app import app
from flask import render_template
from src.services.gridservice import _get_grid_size
from src.services.wordservice import _get_words

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/submit_grid", methods=["POST"])
def create_grid():
    size = _get_grid_size()
    return render_template("submit_grid.html", size=size)

@app.route("/words", methods=["POST"])
def submit_grid():
    words = _get_words()
    return render_template("words.html", words=words)
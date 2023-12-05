from flask import request, render_template

def _get_grid_size():
    return range(int(request.form["size"]))

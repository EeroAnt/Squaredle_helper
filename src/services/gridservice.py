from flask import request, render_template

def _get_grid_size():
    return range(int(request.form["size"]))

def _get_grid_from_input():
	size = int(request.form["size"])
	grid = []
	for i in range(size):
		grid.append([])
		for j in range(size):
			grid[i].append(request.form["{}{}".format(i, j)])
	return grid

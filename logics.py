import random
import time
import threading
from classes import A_star
from algorithms.grid_logic import create_road


def run_taxi(grid, taxi):
    matrix = grid.matrix
    roads = []
    for i, a in enumerate(matrix):
        for j, b in enumerate(a):
            if b > 0:
                roads.append((i, j))
    # print(roads)
    start = A_star.Node(grid, loc=roads[random.randint(0, len(roads))])
    end = A_star.Node(grid, loc=roads[random.randint(0, len(roads))])
    path = A_star.path(start, A_star.search_path(start, end, grid), grid, end)
    taxi.spawn(path[0][0], path[0][1])
    taxi.update_path(path)


def logic(grid, taxis):
    create_road(grid, 40, 20)

    for taxi in taxis:
        threading.Thread(target=run_taxi, args=[grid, taxi], daemon=True).start()

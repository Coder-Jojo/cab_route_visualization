import random
import time
import threading
from classes import A_star
from algorithms.grid_logic import create_road
from classes.spawn import Spawn
from algorithms.infra import backtracking
from algorithms.patches import make_patch


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


def logic(grid, taxis, structures):
    create_road(grid, 40, 20)
    assignments = []
    patches = make_patch(grid)
    dict_of_sizes = {'House':2, 'Indus':5, 'Building':3, 'Tree' : 1, 'Ground':4, 'Airport':7, 'Railway':6}
    for i in patches:
        assignment = backtracking(i, ['Airport','Railway','Indus', 'Ground' , 'Building', 'House', 'Tree'], [],0, 0,0,0)
        assignments.append(assignment)

    for patch_assign in assignments:
        for assigned in patch_assign:
            #print(assigned)
            temp = assigned[:-1][0]
            temp.sort()
            x = temp[0][0]
            y = temp[0][1]
            image2 = Spawn(x,y,dict_of_sizes[assigned[-1]],assigned[-1], grid.size)
            structures.add(image2)
            for indices in assigned[0]:
                grid.matrix[indices[0]][indices[1]] = -1*dict_of_sizes[assigned[-1]]

    grid.create_congestion()

    
    # image_1 = Spawn(2, 2, 3, 'taxi', grid.size)
    # structures.add(image_1)

    for taxi in taxis:
        threading.Thread(target=run_taxi, args=[grid, taxi], daemon=True).start()

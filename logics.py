import random
import time
import threading
from classes import A_star
from algorithms.grid_logic import create_road
from classes.spawn import Spawn
from algorithms.infra import backtracking
from algorithms.patches import make_patch
from algorithms.find_closeness import spawn_taxi


def run_taxi(grid, taxi, start, end, path, person, target):
    taxi_node = A_star.Node(grid, loc=path[0].loc)
    passenger_node = A_star.Node(grid, loc=path[-1].loc)
    path = A_star.path(taxi_node, path, grid, passenger_node)
    taxi.update_path(path)
    person.kill()
    time.sleep(1)
    while taxi.engine_on:
        time.sleep(1)
    path = A_star.path(start, A_star.search_path(start, end, grid, taxi.name), grid, end)
    # taxi.spawn(path[0][0], path[0][1])
    taxi.update_path(path)
    target.kill()


def find_path(grid, location, taxi_list, source, taxi):
    print(taxi, 'is checking distance between itself and the customer')
    x, y = location[0] // grid.size, location[1] // grid.size
    end = A_star.Node(grid, loc=source)
    start = A_star.Node(grid, loc=(x, y))
    path = A_star.search_path(start, end, grid, taxi)
    # path = path[::-1]
    taxi_list.append((len(path), taxi, path))


def find_best_taxi(grid, taxis, source, dest, person, target):
    locations = grid.location
    matrix = grid.matrix
    roads = []
    for i, a in enumerate(matrix):
        for j, b in enumerate(a):
            if b > 0:
                roads.append((i, j))
    # source = 100
    # dest = 1000
    # source = roads[source % len(roads)]
    # dest = roads[dest % len(roads)]

    print('find best taxi near you')
    taxi_list = []
    threads = list()
    for taxi, location in locations.items():
        can_explore = False
        for taxi_ in taxis:
            if taxi_.name == taxi and not taxi_.engine_on:
                can_explore = True
                break
        if not can_explore:
            continue
        process = threading.Thread(target=find_path, args=[grid, location, taxi_list, source, taxi])
        threads.append(process)

    for process in threads:
        process.start()

    for process in threads:
        process.join()

    if not len(taxi_list):
        print('No taxi found near you')
        target.kill()
        person.kill()
        return

    taxi_list.sort(key=lambda x: x[0])

    start = A_star.Node(grid, loc=source)
    end = A_star.Node(grid, loc=dest)
    path = taxi_list[0][-1]

    for length, taxi_name, path in taxi_list:
        required_taxi = None
        for taxi in taxis:
            if taxi.name == taxi_name and not taxi.engine_on:
                required_taxi = taxi
                break
        if required_taxi is not None:
            print(required_taxi.name, 'is your taxi and will be arriving shortly')
            threading.Thread(target=run_taxi, args=[grid, required_taxi, start,
                                                    end, path, person, target], daemon=True).start()
            return
    person.kill()
    target.kill()
    print('No taxi found near you')


def logic(grid, taxis, structures):
    print('creating roads')
    create_road(grid, 40, 20)

    print('calculating best location for taxi spawning')
    spawn_taxi(grid, taxis)

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

    while True:
        time.sleep(1)
        if len(grid.cab_request):
            source, dest, person, target = grid.cab_request[0]
            print('processing the request\nsource:', source, 'dest:', dest)
            process = threading.Thread(target=find_best_taxi, args=[grid, taxis, source, dest, person, target], daemon=True)
            grid.pop()
            process.start()
            process.join()
            # print('done')
    # find_best_taxi(grid, taxis)




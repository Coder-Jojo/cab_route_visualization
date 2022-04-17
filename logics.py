import time
from algorithms.grid_logic import create_road
from classes import A_star


def logic(grid):
    create_road(grid, 40, 20)
    start_x=int(input())
    start_y=int(input())
    end_x=int(input())
    end_y=int(input())
    #x=adjacency.g_value(grid)
    start=adjacency.Node(grid, loc=(start_y,start_x))
    end=adjacency.Node(grid, loc=(end_y, end_x))
    closedList = adjacency.search_path(start, end, grid)
    print(adjacency.path(start, closedList, grid, end))

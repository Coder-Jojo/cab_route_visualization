import time
from algorithms.grid_logic import create_road
from classes import A_star


def logic(grid):
    create_road(grid, 40, 20)
    start_x=int(input())
    start_y=int(input())
    end_x=int(input())
    end_y=int(input())
    #x=A_star.g_value(grid)
    start=A_star.Node(grid, loc=(start_y,start_x))
    end=A_star.Node(grid, loc=(end_y, end_x))
    closedList = A_star.search_path(start, end, grid)
    print(A_star.path(start, closedList, grid, end))

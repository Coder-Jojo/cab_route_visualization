import time
from algorithms import *

def logic(grid):
    i = 0
    while True:
        time.sleep(1)
        grid.update_cell(i, 0, 'red')
        i += 1
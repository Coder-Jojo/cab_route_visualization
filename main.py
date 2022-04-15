import threading

import pygame.sprite

from classes.grid import Grid
from classes.camera import Camera
from classes.taxi import Taxi
from gui import run_gui
from logics import logic


# grid initialization
grid = Grid(100, 100, 50)
grid.initialize_grid()

# camera initialization
camera = Camera(30)

# taxi initialization
taxi_group = pygame.sprite.Group()

taxi_1 = Taxi()
taxi_1.update_path([(0, 1), (1, 1), (1, 2), (1, 3), (2, 3), (3, 3), (3, 4), (3, 5), (4, 5), (4, 4), \
    (5, 4), (6, 4), (7, 4), (8, 4), (9, 4)])
taxi_group.add(taxi_1)

if __name__ == '__main__':

    # running logical part in the different thread to speed the gui
    threading.Thread(target=logic, args=[grid], daemon=True).start()

    # GUI
    run_gui(grid, camera, taxi_group)


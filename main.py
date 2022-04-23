import threading
import pygame.sprite
from classes.grid import Grid
from classes.taxi import Taxi
from gui import run_gui
from logics import logic


# grid initialization
grid = Grid(100, 100, 50)
grid.initialize_grid()

# taxi initialization
taxi_group = pygame.sprite.Group()

# for spawning objects
structures = pygame.sprite.Group()

taxi_1 = Taxi('taxi_1', grid, 'taxi3', speed=6)
taxi_2 = Taxi('taxi_2', grid, 'taxi', speed=4)
taxi_group.add(taxi_1)
taxi_group.add(taxi_2)

taxis = [taxi_1, taxi_2]

if __name__ == '__main__':

    print('starting logical thread')
    threading.Thread(target=logic, args=[grid, taxis, structures], daemon=True).start()

    print('starting the pygame windows')
    run_gui(grid, taxi_group, structures)


import threading
from classes.grid import Grid
from classes.camera import Camera
from gui import run_gui
from logics import logic


# grid initialization
grid = Grid(100, 100, 50)
grid.initialize_grid()

# camera initialization
camera = Camera(30)

if __name__ == '__main__':

    # running logical part in the different thread to speed the gui
    threading.Thread(target=logic, args=[grid], daemon=True).start()

    # GUI
    run_gui(grid, camera)


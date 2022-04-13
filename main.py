import pygame
from sys import exit
from classes.grid import Grid
from classes.camera import Camera

# grid initialization
grid = Grid(100, 100, 50)
grid.update_grid()

# camera initialization
camera = Camera(10)

# screen and pygame initialization
pygame.init()
screen = pygame.display.set_mode((500, 500))
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.fill('grey')
    screen.blit(grid.get_grid(), camera.offset)
    camera.update()
    pygame.display.flip()
    clock.tick(60)

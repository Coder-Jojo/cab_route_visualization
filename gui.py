import pygame
from sys import exit
from classes.camera import Camera


def run_gui(grid, taxi_group):
    pygame.init()
    screen = pygame.display.set_mode((1200, 700))
    clock = pygame.time.Clock()

    # camera initialization
    camera = Camera(30, grid, 1200, 700)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if event.type == pygame.KEYDOWN and event.key == pygame.K_r:
                camera.reset()

            if event.type == pygame.KEYDOWN and event.key == pygame.K_v:
                camera.change()

        screen.fill('black')
        camera.update()
        screen.blit(grid.grid, camera.offset)
        taxi_group.draw(screen)
        taxi_group.update(camera.offset)

        pygame.display.flip()
        clock.tick(32)

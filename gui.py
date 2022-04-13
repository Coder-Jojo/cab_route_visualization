import pygame
from sys import exit


def run_gui(grid, camera):
    pygame.init()
    screen = pygame.display.set_mode((1200, 700))
    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if event.type == pygame.KEYDOWN and event.key == pygame.K_r:
                camera.reset()

        screen.fill('black')
        screen.blit(grid.get_grid(), camera.offset)
        camera.update()
        pygame.display.flip()
        clock.tick(32)

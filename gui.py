import pygame
from sys import exit


def run_gui(grid, camera, taxi_group):
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
        camera.update()
        screen.blit(grid.grid, camera.offset)
        taxi_group.draw(screen)
        taxi_group.update(camera.offset)

        pygame.display.flip()
        clock.tick(32)

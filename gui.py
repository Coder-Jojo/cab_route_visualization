import pygame
from sys import exit
from classes.camera import Camera
from classes.spawn import Spawn

def run_gui(grid, taxi_group, structures):
    pygame.init()
    screen = pygame.display.set_mode((1200, 700))
    clock = pygame.time.Clock()

    # camera initialization
    camera = Camera(30, grid, 1200, 700)

    start, end = None, None
    person = None
    target = None

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if event.type == pygame.KEYDOWN and event.key == pygame.K_r:
                camera.reset()

            if event.type == pygame.KEYDOWN and event.key == pygame.K_v:
                camera.change()

            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                x = int((pos[0] - camera.offset[0]) // grid.size)
                y = int((pos[1] - camera.offset[1]) // grid.size)

                if grid.matrix[x][y] > 0:

                    if start is None:
                        start = (x, y)
                        person = Spawn(x, y, 1, 'person', grid.size)
                        structures.add(person)
                    else:
                        if start[0] == x and start[1] == y:
                            start = None
                            person.kill()
                        else:
                            end = (x, y)
                            target = Spawn(x, y, 1, 'target', grid.size)
                            structures.add(target)

                    if start is not None and end is not None:
                        grid.put(start, end, person, target)
                        start = None
                        end = None

            # if event.type == pygame.KEYDOWN and event.key == pygame.K_c:
            #     camera.switch_camera_type()

        if grid.force_stop is True:
            exit(1)
        screen.fill('black')
        camera.update()
        screen.blit(grid.grid, camera.offset)
        taxi_group.draw(screen)
        taxi_group.update(camera.offset)
        structures.draw(screen)
        structures.update(camera.offset)

        pygame.display.flip()
        clock.tick(32)

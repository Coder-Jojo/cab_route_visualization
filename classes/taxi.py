import math
import random
import pygame


class Taxi(pygame.sprite.Sprite):
    def __init__(self, name, grid, taxi, x=-100, y=-100, size=50, speed=2, color='grey'):
        super().__init__()
        self.image = pygame.image.load(f'./assets/images/{taxi}.png')
        self.image = pygame.transform.scale(self.image, (size, size))
        self.rect = self.image.get_rect(topleft=(x, y))
        self.image = pygame.transform.scale(self.image, (size * .6, size * .9))
        self.left = pygame.transform.rotate(self.image, 90)
        self.right = pygame.transform.rotate(self.image, 270)
        self.top = pygame.transform.rotate(self.image, 0)
        self.bottom = pygame.transform.rotate(self.image, 180)
        self.name = name
        self.grid = grid
        self.x = self.rect.x
        self.y = self.rect.y
        self.speed = speed
        self.engine_on = False
        self.path = []
        self.size = size
        self.color = color
        self.grid.put_taxi(self.name, self.x, self.y)
        self.prev_path = []
        self.congestion = grid.congestion
        self.new_speed = self.speed
        self.col_len = grid.cols

    def update_path(self, path):
        if len(path) == 0:
            return

        path = path[::-1]
        self.engine_on = True
        self.path = []
        self.prev_path = path.copy()

        self.spawn(path[0][0], path[0][1])
        matrix = self.grid.matrix
        for i, a in enumerate(path):
            self.path.append((a[0] * self.size, a[1] * self.size))
            i, j = a
            if matrix[i][j] == 1:
                self.grid.put_vertical_road(i, j, highlight=True)
            elif matrix[i][j] == 2:
                self.grid.put_horizontal_road(i, j, highlight=True)
            elif matrix[i][j] == 3 or matrix[i][j] == 4:
                self.grid.put_intersection(i, j, highlight=True)
        self.grid.special_grid(path[0][0], path[0][1], 'green')
        self.grid.special_grid(path[-1][0], path[-1][1], 'orange')

    def move_right(self):
        self.image = self.right
        self.x += self.new_speed

    def move_left(self):
        self.image = self.left
        self.x -= self.new_speed

    def move_up(self):
        self.image = self.top
        self.y -= self.new_speed

    def move_down(self):
        self.image = self.bottom
        self.y += self.new_speed

    def move_on_path(self):
        if len(self.path) == 0:
            return

        target_x, target_y = self.path[0]
        if target_x == self.x:
            if self.y > target_y:
                self.move_up()
            else:
                self.move_down()
        elif target_y == self.y:
            if self.x < target_x:
                self.move_right()
            else:
                self.move_left()

        if abs(((self.x - target_x) ** 2) - ((self.y - target_y) ** 2)) <= self.speed * self.speed:
            self.x = target_x
            self.y = target_y
            self.path.pop(0)

        self.grid.put_taxi(self.name, self.x, self.y)

    def spawn(self, i, j):
        self.x = i * self.size
        self.y = j * self.size
        self.grid.put_taxi(self.name, self.x, self.y)

    def update(self, offset):
        if not len(self.path):
            self.engine_on = False
            if len(self.prev_path):
                matrix = self.grid.matrix
                for i, a in enumerate(self.prev_path):
                    self.path.append((a[0] * self.size, a[1] * self.size))
                    i, j = a
                    if matrix[i][j] == 1:
                        self.grid.put_vertical_road(i, j)
                    elif matrix[i][j] == 2:
                        self.grid.put_horizontal_road(i, j)
                    elif matrix[i][j] == 3 or matrix[i][j] == 4:
                        self.grid.put_intersection(i, j)
                self.prev_path = []
        if self.engine_on:
            self.move_on_path()
            x = self.x // self.size
            y = self.y // self.size
            self.new_speed = self.speed * (1.1 - 0.5 * self.congestion[int(x * self.col_len + y)])
        self.rect.x = self.x + offset[0]
        self.rect.y = self.y + offset[1]


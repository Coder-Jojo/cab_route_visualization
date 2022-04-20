import pygame
import numpy as np
import math


def congestion_array(rows, cols):
    random_array = abs(np.random.normal(0, 0.5, rows * cols))
    return random_array


def color_ret(random_array, i, j, cols):
    return 255, 255 - min(255, math.floor(255 * random_array[i * cols + j])), 255 - min(255, math.floor(
        255 * random_array[i * cols + j]))


class Grid:
    def __init__(self, rows=100, columns=100, size=20):
        self.rows = rows
        self.cols = columns
        self.size = size
        self.grid = pygame.Surface([rows * size, columns * size])
        self.grid.fill('#567e4a')
        self.matrix = np.zeros((rows, columns))
        self.congestion = congestion_array(rows, columns)
        self.location = dict()

    def initialize_grid(self):
        n = self.rows * self.size
        m = self.cols * self.size
        for i in range(0, n + 1, self.size):
            pygame.draw.line(self.grid, 'black', (0, i), (n, i))
            for j in range(0, m + 1, self.size):
                pygame.draw.line(self.grid, 'black', (j, 0), (j, m))

    def update_cell(self, i, j, color):
        rect = pygame.Rect(i * self.size, j * self.size, self.size, self.size)
        pygame.draw.rect(self.grid, color, rect)

    def put_vertical_road(self, i, j, highlight=False, color='grey'):
        rect1 = pygame.Rect(i * self.size, j * self.size, self.size, self.size)
        # rect2 = pygame.Rect(i * self.size + self.size * .4, j * self.size + self.size * .2, self.size * .2,
        #                     self.size * .6)
        rect2 = pygame.Rect(i * self.size + self.size * .2, j * self.size + self.size * .4, self.size * .6,
                            self.size * .2)
        # if not highlight:
        #     color = color_ret(self.congestion, i, j, self.cols)
        color = color_ret(self.congestion, i, j, self.cols)
        if highlight:
            a, b, c = color
            color = (b, c, a)
            color = (c, a, b)
        pygame.draw.rect(self.grid, color, rect1)
        pygame.draw.rect(self.grid, '#2e2828', rect2)

    def put_horizontal_road(self, i, j, highlight=False, color='grey'):
        rect1 = pygame.Rect(i * self.size, j * self.size, self.size, self.size)
        # rect2 = pygame.Rect(i * self.size + self.size * .2, j * self.size + self.size * .4, self.size * .6,
        #                     self.size * .2)
        rect2 = pygame.Rect(i * self.size + self.size * .4, j * self.size + self.size * .2, self.size * .2,
                            self.size * .6)
        # if not highlight:
        #     color = color_ret(self.congestion, i, j, self.cols)
        color = color_ret(self.congestion, i, j, self.cols)
        if highlight:
            a, b, c = color
            color = (b, c, a)
            color = (c, a, b)
        pygame.draw.rect(self.grid, color, rect1)
        pygame.draw.rect(self.grid, '#2e2828', rect2)

    def put_intersection(self, i, j, highlight=False, color='grey'):
        rect1 = pygame.Rect(i * self.size, j * self.size, self.size, self.size)
        # if not highlight:
        #     color = color_ret(self.congestion, i, j, self.cols)
        color = color_ret(self.congestion, i, j, self.cols)
        if highlight:
            a, b, c = color
            color = (b, c, a)
            color = (c, a, b)
        pygame.draw.rect(self.grid, color, rect1)
        pygame.draw.circle(self.grid, '#2e2828', ((i + .5) * self.size, (j + .5) * self.size), self.size / 4)

    def special_grid(self, i, j, color):
        rect1 = pygame.Rect(i * self.size, j * self.size, self.size, self.size)
        pygame.draw.rect(self.grid, color, rect1)

    def put_taxi(self, name, i, j):
        self.location[name] = (i, j)

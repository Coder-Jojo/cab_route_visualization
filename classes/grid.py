import pygame
import numpy as np


class Grid:
    def __init__(self, rows=100, columns=100, size=20):
        self.rows = rows
        self.cols = columns
        self.size = size
        self.grid = pygame.Surface([rows * size, columns * size])
        self.grid.fill('#567e4a')
        self.matrix = np.zeros((rows, columns))

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

    def put_vertical_road(self, i, j):
        rect1 = pygame.Rect(i * self.size, j * self.size, self.size, self.size)
        rect2 = pygame.Rect(i * self.size + self.size * .4, j * self.size + self.size * .2, self.size * .2, self.size * .6)
        pygame.draw.rect(self.grid, 'grey', rect1)
        pygame.draw.rect(self.grid, 'white', rect2)

    def put_horizontal_road(self, i, j):
        rect1 = pygame.Rect(i * self.size, j * self.size, self.size, self.size)
        rect2 = pygame.Rect(i * self.size + self.size * .2, j * self.size + self.size * .4, self.size * .6, self.size * .2)
        pygame.draw.rect(self.grid, 'grey', rect1)
        pygame.draw.rect(self.grid, 'white', rect2)

    def put_intersection(self, i, j):
        rect1 = pygame.Rect(i * self.size, j * self.size, self.size, self.size)
        pygame.draw.rect(self.grid, 'grey', rect1)
        pygame.draw.circle(self.grid, 'white', ((i + .5) * self.size, (j + .5) * self.size), self.size / 4)


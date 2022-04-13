import pygame


class Grid:
    def __init__(self, rows=20, columns=20, size=20):
        self.rows = rows
        self.cols = columns
        self.size = size
        self.grid = pygame.Surface([rows * size, columns * size], pygame.SRCALPHA, 32)

    def update_grid(self):
        n = self.rows * self.size
        m = self.cols * self.size
        for i in range(0, n, self.size+1):
            pygame.draw.line(self.grid, 'black', (0, i), (n, i))
            for j in range(0, m, self.size+1):
                pygame.draw.line(self.grid, 'black', (j, 0), (j, m))

    def update_cell(self, i, j, color):
        rect = pygame.Rect(i, j, self.size, self.size)
        pygame.draw.rect(self.grid, color, rect)

    def get_grid(self):
        return self.grid
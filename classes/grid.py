import pygame
import numpy as np
import math

def check_valid(grid,i,j):
    if(i<0 or i>=100 or j<0 or j>= 100 ):
        return False
    if(grid.matrix[i][j]>=0):
        return False
    return True

def congestion_array(grid):
    print(grid.matrix)
    congested = []
    for i in range(grid.rows):
        for j in range(grid.cols):
            sum = 0
            if(grid.matrix[i][j]>0):
                #print("Found")
                if(check_valid(grid,i-1,j)): #left
                    sum += (-1)*grid.matrix[i-1][j]
                if(check_valid(grid,i+1,j)): #right
                    sum += (-1)*grid.matrix[i+1][j]
                if(check_valid(grid,i,j-1)): #up
                    sum += (-1)*grid.matrix[i][j-1]
                if(check_valid(grid,i,j+1)): #down
                    sum += (-1)*grid.matrix[i][j+1]
            congested.append(float(sum)/28)
    #print(congested)
    return congested
            
                

    


def color_ret(random_array, i, j, cols):
    return 255, 255 - min(255, math.floor(255 * random_array[i * cols + j])), 255 - min(255, math.floor(
        255 * random_array[i * cols + j]))


class Grid:
    def __init__(self, rows=100, columns=100, size=20):
        self.rows = rows
        self.cols = columns
        self.size = size
        self.grid = pygame.Surface([rows * size, columns * size])
        self.grid.fill('#0b8a33')
        self.matrix = np.zeros((rows, columns))
        self.congestion = np.zeros(rows*columns)
        self.location = dict()
        self.path = dict()
        self.force_stop = False
        self.cab_request = list()

    def initialize_grid(self):
        n = self.rows * self.size
        m = self.cols * self.size
        for i in range(0, n + 1, self.size):
            pygame.draw.line(self.grid, '#096e29', (0, i), (n, i))
            for j in range(0, m + 1, self.size):
                pygame.draw.line(self.grid, '#096e29', (j, 0), (j, m))

    def update_cell(self, i, j, color):
        rect = pygame.Rect(i * self.size, j * self.size, self.size, self.size)
        pygame.draw.rect(self.grid, color, rect)

    def put_vertical_road(self, i, j, highlight=False, color=None):
        rect1 = pygame.Rect(i * self.size, j * self.size, self.size, self.size)
        rect2 = pygame.Rect(i * self.size + self.size * .2, j * self.size + self.size * .4, self.size * .6,
                            self.size * .2)
        new_color = color_ret(self.congestion, i, j, self.cols)
        if highlight:
            a, b, c = new_color
            new_color = (c, a, b)
        if color is None:
            color = new_color
        pygame.draw.rect(self.grid, color, rect1)
        pygame.draw.rect(self.grid, '#424242', rect2)

    def put_horizontal_road(self, i, j, highlight=False, color=None):
        rect1 = pygame.Rect(i * self.size, j * self.size, self.size, self.size)
        rect2 = pygame.Rect(i * self.size + self.size * .4, j * self.size + self.size * .2, self.size * .2,
                            self.size * .6)
        new_color = color_ret(self.congestion, i, j, self.cols)
        if highlight:
            a, b, c = new_color
            new_color = (c, a, b)
        if color is None:
            color = new_color
        pygame.draw.rect(self.grid, color, rect1)
        pygame.draw.rect(self.grid, '#424242', rect2)

    def put_intersection(self, i, j, highlight=False, color=None):
        rect1 = pygame.Rect(i * self.size, j * self.size, self.size, self.size)
        new_color = color_ret(self.congestion, i, j, self.cols)
        if highlight:
            a, b, c = new_color
            new_color = (c, a, b)
        if color is None:
            color = new_color
        pygame.draw.rect(self.grid, color, rect1)
        pygame.draw.circle(self.grid, '#424242', ((i + .5) * self.size, (j + .5) * self.size), self.size / 4)

    def special_grid(self, i, j, color):
        rect1 = pygame.Rect(i * self.size, j * self.size, self.size, self.size)
        pygame.draw.rect(self.grid, color, rect1)

    def put_taxi(self, name, i, j):
        self.location[name] = (i, j)

    def create_congestion(self):
        self.congestion = congestion_array(self)
        self.update_congested_road()

    def update_congested_road(self):
        road = []
        for i in range(self.rows):
            for j in range(self.cols):
                if self.matrix[i][j] != 0:
                # road.append((j, i, matrix[i][j]))
                    road.append((i, j, self.matrix[i][j]))

        for x, y, z in road:
            if z == 1:
                self.put_vertical_road(x, y)
            elif z == 2:
                self.put_horizontal_road(x, y)
            elif z == 3 or z == 4:
                self.put_intersection(x, y)

    def put_path(self, name, i, j):
        self.path[name] = (i, j)

    def a_star_cells(self, x, y, color):
        z = self.matrix[x][y]
        if z == 1:
            self.put_vertical_road(x, y, color=color)
        elif z == 2:
            self.put_horizontal_road(x, y, color=color)
        elif z == 3 or z == 4:
            self.put_intersection(x, y, color=color)

    def get_back_congestion_road(self, nodes):
        for x, y in nodes:
            z = self.matrix[x][y]
            if z == 1:
                self.put_vertical_road(x, y)
            elif z == 2:
                self.put_horizontal_road(x, y)
            elif z == 3 or z == 4:
                self.put_intersection(x, y)

    def force_stop(self):
        self.force_stop = True

    def put(self, source, dest, person, target):
        self.cab_request.append((source, dest, person, target))

    def pop(self):
        self.cab_request.pop(0)


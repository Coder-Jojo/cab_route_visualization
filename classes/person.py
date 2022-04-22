import pygame


class Person:
    def __init__(self, grid, size=50):
        self.image = pygame.image.load('../assets/images/person.png')
        self.image = pygame.transform.scale(self.image, (size, size))
        self.grid = grid
        self.size = size
        self.passengers = []

    def put_passenger(self, i, j):
        self.passengers.append((i, j))

    def remove_passenger(self, i, j):
        self.passengers = filter(lambda x: x != (i, j), self.passengers)

    def update(self):
        for passenger in self.passengers:
            self.grid.grid.blit(self.image, passenger)
import math
import random
import pygame


class Taxi(pygame.sprite.Sprite):
    def __init__(self, x=0, y=0, size=50, speed=2):
        super().__init__()
        self.image = pygame.image.load('./assets/images/taxi3.png')
        self.image = pygame.transform.scale(self.image, (size, size))
        self.rect = self.image.get_rect(topleft=(x, y))
        self.image = pygame.transform.scale(self.image, (size * .6, size * .9))
        self.left = pygame.transform.rotate(self.image, 90)
        self.right = pygame.transform.rotate(self.image, 270)
        self.top = pygame.transform.rotate(self.image, 0)
        self.bottom = pygame.transform.rotate(self.image, 180)
        self.x = self.rect.x
        self.y = self.rect.y
        self.speed = speed
        self.engine_on = False
        self.path = []
        self.size = size

    def update_path(self, path):
        if len(path):
            self.engine_on = True
            self.path = []

        for i, a in enumerate(path):
            self.path.append((a[0] * self.size, a[1] * self.size))

    def move_right(self):
        self.image = self.right
        self.x += self.speed

    def move_left(self):
        self.image = self.left
        self.x += self.speed

    def move_up(self):
        self.image = self.top
        self.y -= self.speed

    def move_down(self):
        self.image = self.bottom
        self.y += self.speed

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

    def update(self, offset):
        if not len(self.path):
            self.engine_on = False
        if self.engine_on:
            self.move_on_path()
        self.rect.x = self.x + offset[0]
        self.rect.y = self.y + offset[1]

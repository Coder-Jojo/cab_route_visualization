import pygame


class Camera:
    def __init__(self, speed):
        self.i = 0
        self.j = 0
        self.speed = speed

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.i += self.speed
        elif keys[pygame.K_d]:
            self.i -= self.speed
        elif keys[pygame.K_w]:
            self.j += self.speed
        elif keys[pygame.K_s]:
            self.j -= self.speed

    def reset(self):
        self.i, self.j = 0, 0

    @property
    def offset(self):
        off = (self.i, self.j)
        return off

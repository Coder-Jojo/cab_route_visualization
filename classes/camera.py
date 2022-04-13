import pygame


class Camera:
    def __init__(self, speed):
        self.i = 0
        self.j = 0
        self.speed = speed

    def move_left(self):
        self.j += self.speed

    def move_right(self):
        self.j -= self.speed

    def move_down(self):
        self.i -= self.speed

    def move_up(self):
        self.i += self.speed

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

        # self.i = max(0, self.i)
        # self.j = max(0, self.j)

    @property
    def offset(self):
        off = (self.i, self.j)
        return off

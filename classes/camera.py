import pygame


class Camera:
    def __init__(self, speed, grid, winx, winy):
        self.i = 0
        self.j = 0
        self.speed = speed
        self.camera_type = 0
        self.taxi = (0, 0)
        self.winX = winx / 2
        self.winY = winy / 2
        self.grid = grid

    def move_with_keyboard(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.i += self.speed
        elif keys[pygame.K_d]:
            self.i -= self.speed
        elif keys[pygame.K_w]:
            self.j += self.speed
        elif keys[pygame.K_s]:
            self.j -= self.speed

    def focus_taxi(self):
        self.i = -self.grid.location[self.taxi][0] + self.winX
        self.j = -self.grid.location[self.taxi][1] + self.winY

    def update(self):
        if self.camera_type == 0:
            self.move_with_keyboard()
        elif self.camera_type >= 1:
            self.focus_taxi()

    def reset(self):
        self.i, self.j = 0, 0

    def change(self):
        self.camera_type += 1
        self.camera_type %= (len(self.grid.location.keys()) + 1)
        if self.camera_type > 0:
            self.taxi = sorted(list(self.grid.location.keys()))[self.camera_type - 1]

    @property
    def offset(self):
        off = (self.i, self.j)
        return off

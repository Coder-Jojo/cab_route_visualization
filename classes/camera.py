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
        self.path = 0
        self.switch_camera = 0

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

    def over_power_span(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a] or keys[pygame.K_d] or keys[pygame.K_a] or keys[pygame.K_s]:
            self.camera_type = 0
        # elif keys[pygame.K_d]:
        #     self.i -= self.speed
        # elif keys[pygame.K_w]:
        #     self.j += self.speed
        # elif keys[pygame.K_s]:
        #     self.j -= self.speed

    def focus_taxi(self):
        self.i = -self.grid.location[self.taxi][0] + self.winX
        self.j = -self.grid.location[self.taxi][1] + self.winY

    # def focus_path(self):
    #     self.i = -self.grid.path[self.path][0] + self.winX
    #     self.j = -self.grid.path[self.path][1] + self.winY

    def update(self):
        if self.camera_type == 0:
            self.move_with_keyboard()
        elif self.camera_type >= 1:
            self.focus_taxi()
        self.over_power_span()
        # if self.switch_camera == 0:
        #     if self.camera_type == 0:
        #         self.move_with_keyboard()
        #     elif self.camera_type >= 1:
        #         self.focus_taxi()
        # elif self.switch_camera == 1:
        #     if self.camera_type == 0:
        #         self.move_with_keyboard()
        #     else:
        #         self.focus_path()

    def reset(self):
        self.i, self.j = 0, 0

    def change(self):
        self.camera_type += 1
        # if self.camera_type > 0:
        #     if self.switch_camera == 0:
        self.camera_type %= (len(self.grid.location.keys()) + 1)
        self.taxi = sorted(list(self.grid.location.keys()))[self.camera_type - 1]
            # elif self.switch_camera == 1:
            #     if len(self.grid.path.keys()) == 0:
            #         self.camera_type = 0
            #         return
            #     self.camera_type %= (len(self.grid.path.keys()) + 1)
            #     self.path = sorted(list(self.grid.path.keys()))[self.camera_type - 1]

    # def switch_camera_type(self):
    #     self.switch_camera = (self.switch_camera + 1) % 2
    #     self.change()
    #     print(self.switch_camera)

    @property
    def offset(self):
        off = (self.i, self.j)
        return off

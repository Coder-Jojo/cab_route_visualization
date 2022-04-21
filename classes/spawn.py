import pygame


class Spawn(pygame.sprite.Sprite):
    def __init__(self, i, j, scale, image, size):
        super().__init__()
        self.image = pygame.image.load(f'./assets/images/{image}.png')
        self.image = pygame.transform.scale(self.image, (size * scale, size * scale))
        self.rect = self.image.get_rect(topleft=(i*size, j*size))
        self.x = self.rect.x
        self.y = self.rect.y

    def update(self, offset):
        self.rect.x = self.x + offset[0]
        self.rect.y = self.y + offset[1]
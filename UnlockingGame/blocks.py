from os import X_OK
import pygame
import os

IMG_DIR = os.path.dirname(__file__)
print(IMG_DIR)


class Platform(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load("%s/img/blocks/platform.png" % IMG_DIR)
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.type = "solid"
        self.rect.x = x
        self.rect.y = y


class Finish(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load("%s/img/blocks/finish.png" % IMG_DIR)
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.type = "finish"
        self.rect.x = x
        self.rect.y = y


class Obstacle(pygame.sprite.Sprite):
    def __init__(self, x, y, a):
        super().__init__()
        self.image = pygame.image.load("%s/img/blocks/obstacle.png" % IMG_DIR)
        self.image = pygame.transform.rotate(self.image, a*90)
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.type = "obstacle"
        self.rect.x = x
        self.rect.y = y

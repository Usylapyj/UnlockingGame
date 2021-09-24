from os import X_OK
import pygame


class Platform(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load("img/blocks/platform.png")
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.type = "solid"
        self.rect.x = x
        self.rect.y = y


class Finish(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load("img/blocks/finish.png")
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.type = "finish"
        self.rect.x = x
        self.rect.y = y


class Obstacle(pygame.sprite.Sprite):
    def __init__(self, x, y, a):
        super().__init__()
        self.image = pygame.image.load("img/blocks/obstacle.png")
        self.image = pygame.transform.rotate(self.image, a*90)
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.type = "obstacle"
        self.rect.x = x
        self.rect.y = y

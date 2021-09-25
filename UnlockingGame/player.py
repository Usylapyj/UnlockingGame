import pygame
import pygame.mask
import os

IMG_DIR = os.path.dirname(__file__)
print(IMG_DIR)


class Player(pygame.sprite.Sprite):

    def __init__(self, startx, starty, jump_power, speed, gravity):
        super().__init__()

        self.jump_power = jump_power
        self.speed = speed
        self.gravity = gravity
        self.startx = startx
        self.starty = starty

        self.xvel = 0.
        self.yvel = 0.
        self.left = 0
        self.right = 0
        self.on_ground = False
        self.jumps = 0

        self.image_left = pygame.image.load("%s/img/player/left.png" % IMG_DIR)
        self.image_right = pygame.image.load(
            "%s/img/player/right.png" % IMG_DIR)
        self.image = self.image_right
        self.rect = self.image.get_rect()
        self.rect.x = self.startx
        self.rect.y = self.starty

        self.mask = pygame.mask.from_surface(pygame.Surface((self.rect.width,
                                                             self.rect.height)))

    def update(self, objects):
        self.xvel = (self.right - self.left) * self.speed

        if not self.on_ground:
            self.yvel += self.gravity

        self.rect.y += self.yvel
        f = self.collide(0, self.yvel, objects)

        self.rect.x += self.xvel
        f *= self.collide(self.xvel, 0, objects)
        return f

    def jump(self):

        if self.on_ground:
            self.on_ground = False
            self.yvel = -self.jump_power
        elif self.jumps < 2:
            self.jumps += 1
            self.yvel = -self.jump_power

    def stop_jump(self):
        if self.yvel < 0:
            self.yvel = 0

    def collide(self, xvel, yvel, blocks):
        f = False
        down_mask = pygame.mask.from_surface(pygame.Surface((1, 32)))
        for p in blocks:
            if pygame.sprite.collide_mask(self, p):
                if p.type == "finish":
                    f = True
                elif p.type == "obstacle":
                    self.set_pose(self.startx, self.starty)
                    self.xvel = 0
                    self.yvel = 0
                elif p.type == "solid":
                    if xvel > 0:
                        self.rect.right = p.rect.left

                    if xvel < 0:
                        self.rect.left = p.rect.right

                    if yvel > 0:
                        self.rect.bottom = p.rect.top
                        self.yvel = 0
                        self.on_ground = True
                        self.jumps = 0

                    if yvel < 0:
                        self.rect.top = p.rect.bottom
                        self.yvel = 0
            if self.mask.overlap_area(p.mask, (self.rect.x, self.rect.y+33)) > 0:
                print(self.mask.overlap_area(
                    p.mask, (self.rect.x, self.rect.y+33)))
                self.on_ground = True
                self.jumps = 0
        else:
            self.on_ground = False
        return f

    def set_pose(self, x, y):
        self.rect.x = x
        self.rect.y = y

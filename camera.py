import pygame


class Camera(object):
    def __init__(self, width, height, total_width, total_height):
        self.total_width = total_width
        self.total_height = total_height
        self.width = width
        self.height = height
        self.state = pygame.Rect(0, 0, width, height)

    def apply(self, target):
        return target.rect.move(self.state.topleft)

    def update(self, target):
        self.state = self.configure(target.rect)

    def configure(self, target_rect):
        l, t, _, _ = target_rect
        _, _, w, h = self.state
        l, t = -l+self.width / 2, -t+self.height / 2

        l = min(0, l)
        l = max(-(self.total_width-self.width), l)
        t = max(-(self.total_height-self.height), t)
        t = min(0, t)

        return pygame.Rect(l, t, w, h)

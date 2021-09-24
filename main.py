from camera import Camera
import pygame
import pygame.transform
from player import Player
from blocks import Platform, Finish, Obstacle
from keyboard_locker import KeyboardLocker

# window properties
WIN_WIDTH = 640
WIN_HEIGHT = 640
MAX_FPS = 60

# player properties
JUMP_POWER = 17
SPEED = 7
GRAVITY = 1


class Game:
    def __init__(self, win_width, win_height, max_fps):

        self.win_width = win_width
        self.win_height = win_height
        self.max_fps = max_fps

        self.blocks = []

        pygame.init()

        WIN_WIDTH = pygame.display.Info().current_w
        WIN_HEIGHT = pygame.display.Info().current_h

        self.keyboard_locker = KeyboardLocker()
        self.keyboard_locker.start()

        self.clock = pygame.time.Clock()
        self.objects = pygame.sprite.Group()
        pygame.display.init()
        self.screen = pygame.display.set_mode((WIN_WIDTH,
                                               WIN_HEIGHT),
                                              pygame.NOFRAME | pygame.SCALED)  # (0, 0), pygame.FULLSCREEN

        self.level_width, self.level_height = self.load_level()

        self.camera = Camera(WIN_WIDTH, WIN_HEIGHT,
                             self.level_width, self.level_height)

        self.running = True

    def mainloop(self):
        while self.running:
            self.handle_events()
            self.update()
            self.draw()
            # print(self.player.on_ground, '\t', self.player.jumps)

            self.clock.tick(self.max_fps)

    def handle_events(self):
        events = pygame.event.get()

        for event in events:
            if event.type == pygame.QUIT:
                self.finish_game()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.finish_game()
                if event.key == pygame.K_LEFT:
                    self.player.left = 1
                if event.key == pygame.K_RIGHT:
                    self.player.right = 1
                if event.key == pygame.K_x:
                    self.player.jump()

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    self.player.left = 0
                if event.key == pygame.K_RIGHT:
                    self.player.right = 0
                if event.key == pygame.K_x:
                    self.player.stop_jump()

    def update(self):
        if self.player.update(self.blocks):
            self.finish_game()
        self.camera.update(self.player)

    def draw(self):
        self.screen.fill([148, 0, 212])
        for e in self.objects:
            # if e.rect.colliderect(self.camera.configure(self.player.rect)):
            self.screen.blit(e.image, self.camera.apply(e))
        pygame.display.update()

    def finish_game(self):
        self.keyboard_locker.stop()
        raise SystemExit

    def get_level(self):
        level_map = ["111111111111111111111111111111",
                     "6 4   4 4   2       4     4 31",
                     "6             121       1   31",
                     "6    2 2 2 2 2 1   315      31",
                     "1  11111115111 4 2  4      111",
                     "11 41    15      1315        1",
                     "14       15      4           1",
                     "12    12215    315        2221",
                     "111  31  4      4    2   31111",
                     "1           222      1    4441",
                     "1222       31111  1  1 31   31",
                     "11111    1           1  4   31",
                     "1   122                     31",
                     "1   111                   3111",
                     "1             2         2    1",
                     "1           31115  2    1    1",
                     "1                  1    1    1",
                     "1   2 2222 2222222212222122221",
                     "111111111111111111111111111111"
                     ]
        start_pose = (1, 1)

        return level_map, start_pose

    def load_level(self):
        level_map, start_pose = self.get_level()

        self.player = Player(start_pose[0]*64,
                             start_pose[1]*64,
                             JUMP_POWER, SPEED, GRAVITY)
        self.objects.add(self.player)

        for y in range(len(level_map)):
            for x in range(len(level_map[y])):
                if level_map[y][x] == '1':
                    b = Platform(x*64, y*64)
                elif level_map[y][x] == '6':
                    b = Finish(x*64, y*64)
                elif level_map[y][x] == '2':
                    b = Obstacle(x*64, y*64, 0)
                elif level_map[y][x] == '3':
                    b = Obstacle(x*64, y*64, 1)
                elif level_map[y][x] == '4':
                    b = Obstacle(x*64, y*64, 2)
                elif level_map[y][x] == '5':
                    b = Obstacle(x*64, y*64, 3)
                self.objects.add(b)
                self.blocks.append(b)

        return len(level_map[0])*64, len(level_map)*64


def main():
    game = Game(WIN_WIDTH, WIN_HEIGHT, MAX_FPS)
    game.mainloop()


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        with open('exeption.log', 'w') as f:
            f.write(e)


'''
rgb(148,0,212)
'''

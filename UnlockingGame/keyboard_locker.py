import threading
import pygame
import Xlib.display
import Xlib.X


class KeyboardLocker(threading.Thread):
    keys_dict = {113: 1073741904,
                 114: 1073741903,
                 53: 120,
                 9: 27}

    def __init__(self):
        super().__init__()
        self.running = True
        self.display = Xlib.display.Display()
        self.root = self.display.screen().root

    def run(self):
        self.root.change_attributes(
            event_mask=Xlib.X.KeyPressMask | Xlib.X.KeyReleaseMask)

        self.root.grab_keyboard(False, Xlib.X.GrabModeSync,
                                Xlib.X.GrabModeAsync, Xlib.X.CurrentTime)

        self.display.change_keyboard_control(
            auto_repeat_mode=Xlib.X.AutoRepeatModeOff)
        while self.running:
            event = self.display.next_event()
            if event.type == 2:
                if event.detail in self.keys_dict.keys():
                    a = pygame.event.Event(pygame.KEYDOWN,
                                           key=self.keys_dict[event.detail])
                    pygame.event.post(a)
            elif event.type == 3:
                if event.detail in self.keys_dict.keys():
                    a = pygame.event.Event(pygame.KEYUP,
                                           key=self.keys_dict[event.detail])
                    pygame.event.post(a)
        self.display.ungrab_keyboard(Xlib.X.CurrentTime)
        self.display.change_keyboard_control(
            auto_repeat_mode=Xlib.X.AutoRepeatModeOn)
        self.root.grab_keyboard(False, Xlib.X.GrabModeSync,
                                Xlib.X.GrabModeAsync, Xlib.X.CurrentTime)

    def stop(self):
        self.running = False

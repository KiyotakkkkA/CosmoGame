from Utility.GlobalSettings import *
import pygame as pg

from GameClasses.Interface.ClassInterface import Interface



class Button(Interface):
    def __init__(self, sc, x, y, txt, command=None, radius=50, animation_type='circle', color=WHITE):
        super().__init__()
        self.sc = sc
        self.x = x
        self.y = y
        self.radius = radius

        self.color = color
        self.active_color1 = LIGHT_BLUE

        self.animation_type = animation_type

        self.offset_x = self.text_width // 4

        self.key = [0, 0]

        self.modify = False
        self.command = command
        self.txt = txt


    def draw(self):
        mouse_pos = pg.mouse.get_pos()
        click = pg.mouse.get_pressed()

        if self.animation_type == 'circle':
            distance = ((mouse_pos[0] - (self.x + self.radius)) ** 2 + (mouse_pos[1] - (self.y + self.radius)) ** 2) ** 0.5
            if distance <= self.radius:
                pg.draw.circle(self.sc, WHITE, [self.x + self.radius, self.y + self.radius], self.radius, 2)
                pg.draw.circle(self.sc, LIGHT_BLUE, [self.x + self.radius, self.y + self.radius], self.radius-2)

                if click[0]:
                    self.key[0] = 1
                if not click[0] and self.key[0]:
                    self.key[1] = 1

            self.many_text(self.sc, self.x + self.radius * len(self.txt) // 3.5, self.y + self.text_height // 1.75,
                           self.txt, self.color, modify=self.modify)

        if self.animation_type == 'rectangle':
            width = len(self.txt[0]) * (self.text_width)
            height = self.text_height

            # buttons hitbox
            # pg.draw.rect(self.sc, WHITE, [self.x + self.offset_x, (self.y - height // 4) + height, width, height], 1)
            if (self.x + self.offset_x < mouse_pos[0] < self.x + width + self.offset_x) and \
                    (((self.y - height // 4) + height) < mouse_pos[1] < (self.y - height // 4) + height * 2):

                if click[0]:
                    self.key[0] = 1
                if not click[0] and self.key[0]:
                    self.key[1] = 1

                self.many_text(self.sc, self.x + self.radius * len(self.txt) // 3.5, self.y + self.text_height // 1.75,
                               self.txt, self.active_color1)

            else:
                self.many_text(self.sc, self.x + self.radius * len(self.txt) // 3.5, self.y + self.text_height // 1.75,
                               self.txt, self.color)

        if all(self.key) and self.command is not None:

            self.command()
            self.key = [0, 0]




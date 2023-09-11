import pygame as pg
from Utility.GlobalSettings import WHITE, FPS

from Database import *

class Interface:
    pg.init()
    def __init__(self):
        self.size = 40
        self.font = 'Assets/Fonts/SEI.ttf'

        self.clock = pg.time.Clock()
        self.FPS = FPS

        self.run = False
        self.run_settings = False
        self.run_menu = True

        self.key = 0
        self.animation_mouse_pos = [0, 0]
        self.animation_queue = []
        self.animation_counter = 0

        self.destroy_animation_queue = []

        self.text_height = 38
        self.text_width = 36

        self.rendered = pg.font.Font(self.font, self.size)

        def bind():
            keys = get_data(data, 'control')
            self.control_dict = {'up': [keys[0][1], keys[0][2]],
                            'down': [keys[1][1], keys[1][2]],
                            'left': [keys[2][1], keys[2][2]],
                            'right': [keys[3][1], keys[3][2]]
                            }

        if get_data(data, 'control'):
            bind()

        if not get_data(data, 'control'):
            enter(data, ['w', pg.K_w], 'control', 1)
            enter(data, ['s', pg.K_s], 'control', 1)
            enter(data, ['a', pg.K_a], 'control', 1)
            enter(data, ['d', pg.K_d], 'control', 1)

            self.control_dict = {'up': ['w', 119],
                            'down': ['s', 115],
                            'left': ['a', 97],
                            'right': ['d', 100]
                            }
    def change_font(self, size, font):
        self.size = size
        self.font = font

        self.rendered = pg.font.Font(self.font, self.size)

    def draw_button(self, screen, coordinates, color_mode):
        m_x, m_y = pg.mouse.get_pos()
        if coordinates[0] <= m_x <= coordinates[0] + coordinates[2] and coordinates[1] <= m_y <= coordinates[1] + coordinates[3]:
            pg.draw.rect(screen, color_mode, [coordinates[0] + 1, coordinates[1] + 1, coordinates[2] - 1, coordinates[3] - 1])
        pg.draw.rect(screen, WHITE, (coordinates[0], coordinates[1], coordinates[2], coordinates[3]), 1)

    def text(self, screen, x, y, text, color, modify=False):
        if not modify:
            text_ = self.rendered.render(text, True, color)
            screen.blit(text_, (x, y))
        if modify == 'underline':
            self.rendered.set_underline(True)
            text_ = self.rendered.render(text, True, color)
            screen.blit(text_, (x, y))


    def many_text(self, screen, x, y, text_array, color, modify=False):
        dy = 0
        for i in text_array:
            self.text(screen, x, y + dy, i, color, modify)
            dy += self.size

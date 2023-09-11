from GameClasses.Interface.ClassInterface import Interface
from GameClasses.Tiles.ClassButton import Button
from GameClasses.Tiles.ClassMouseEffect import MouseEffect

from RenderedMedia import menu_space_bg

from Utility.GlobalSettings import *

import pygame as pg
import sys

class Settings(Interface):
    def __init__(self):
        super().__init__()

        self.settings_screen = pg.display.set_mode((WIDTH, HEIGHT))

        self.bg = pg.transform.scale(menu_space_bg, (WIDTH, HEIGHT))

        self.need_draw_click = False

        self.settings_buttons = []

    def render_text(self):
        self.many_text(self.settings_screen, 20, HEIGHT * 0.01 + self.text_height * 1.5, [f'Вперёд: '], WHITE)
        self.many_text(self.settings_screen, 20, HEIGHT * 0.01 + self.text_height * 3, [f'Назад: '], WHITE)
        self.many_text(self.settings_screen, 20, HEIGHT * 0.01 + self.text_height * 4.5, [f'Влево: '], WHITE)
        self.many_text(self.settings_screen, 20, HEIGHT * 0.01 + self.text_height * 6, [f'Вправо:'], WHITE)

    def update_buttons(self):

        def back():
            from main import app
            self.run_settings = not self.run_settings
            self.run_menu = not self.run_menu
            app.show_menu()

        self.settings_buttons = [
            Button(self.settings_screen, WIDTH * 0.07, HEIGHT - self.text_height * 2, ['Назад'],
                   animation_type='rectangle', command=back),
            Button(self.settings_screen, WIDTH * 0.07 + 200, HEIGHT - self.text_height * 2, ['Сбросить'],
                   animation_type='rectangle', command=self.return_back),

            Button(self.settings_screen, WIDTH * 0.07 + 470,
                   HEIGHT * 0.01 + self.text_height * 1.5 - self.text_height // 2, [f'{self.control_dict["up"][0]}'],
                   animation_type='rectangle', command=self.rebind_up),
            Button(self.settings_screen, WIDTH * 0.07 + 470,
                   HEIGHT * 0.01 + self.text_height * 3 - self.text_height // 2, [f'{self.control_dict["down"][0]}'],
                   animation_type='rectangle', command=self.rebind_down),
            Button(self.settings_screen, WIDTH * 0.07 + 470,
                   HEIGHT * 0.01 + self.text_height * 4.5 - self.text_height // 2, [f'{self.control_dict["left"][0]}'],
                   animation_type='rectangle', command=self.rebind_left),
            Button(self.settings_screen, WIDTH * 0.07 + 470,
                   HEIGHT * 0.01 + self.text_height * 6 - self.text_height // 2, [f'{self.control_dict["right"][0]}'],
                   animation_type='rectangle', command=self.rebind_right),
        ]

    def rebind_up(self):
        choose = True
        while choose:
            for j in pg.event.get():
                if j.type == pg.QUIT:
                    sys.exit()
                if j.type == pg.KEYDOWN:
                    if int(j.key) in id_dict:
                        self.control_dict['up'][0] = id_dict[int(j.key)]
                        self.control_dict['up'][1] = int(j.key)
                        update_db(data, 'key', 'control', id_dict[int(j.key)], 1)
                        update_db(data, 'value', 'control', int(j.key), 1)
                        choose = False

        self.update_buttons()

    def rebind_down(self):
        choose = True
        while choose:
            for j in pg.event.get():
                if j.type == pg.QUIT:
                    sys.exit()
                if j.type == pg.KEYDOWN:
                    if int(j.key) in id_dict:
                        self.control_dict['down'][0] = id_dict[int(j.key)]
                        self.control_dict['down'][1] = int(j.key)
                        update_db(data, 'key', 'control', id_dict[int(j.key)], 2)
                        update_db(data, 'value', 'control', int(j.key), 2)
                        choose = False

        self.update_buttons()

    def rebind_left(self):
        choose = True
        while choose:
            for j in pg.event.get():
                if j.type == pg.QUIT:
                    sys.exit()
                if j.type == pg.KEYDOWN:
                    if int(j.key) in id_dict:
                        self.control_dict['left'][0] = id_dict[int(j.key)]
                        self.control_dict['left'][1] = int(j.key)
                        update_db(data, 'key', 'control', id_dict[int(j.key)], 3)
                        update_db(data, 'value', 'control', int(j.key), 3)
                        choose = False
        self.update_buttons()

    def rebind_right(self):
        choose = True
        while choose:
            for j in pg.event.get():
                if j.type == pg.QUIT:
                    sys.exit()
                if j.type == pg.KEYDOWN:
                    if int(j.key) in id_dict:
                        self.control_dict['right'][0] = id_dict[int(j.key)]
                        self.control_dict['right'][1] = int(j.key)
                        update_db(data, 'key', 'control', id_dict[int(j.key)], 4)
                        update_db(data, 'value', 'control', int(j.key), 4)
                        choose = False
        self.update_buttons()

    def return_back(self):
        self.control_dict['right'][0] = 'd'
        self.control_dict['right'][1] = pg.K_d
        update_db(data, 'key', 'control', 'd', 4)
        update_db(data, 'value', 'control', pg.K_d, 4)

        self.control_dict['up'][0] = 'w'
        self.control_dict['up'][1] = pg.K_w
        update_db(data, 'key', 'control', 'w', 1)
        update_db(data, 'value', 'control', pg.K_w, 1)

        self.control_dict['down'][0] = 's'
        self.control_dict['down'][1] = pg.K_s
        update_db(data, 'key', 'control', 's', 2)
        update_db(data, 'value', 'control', pg.K_s, 2)

        self.control_dict['left'][0] = 'a'
        self.control_dict['left'][1] = pg.K_a
        update_db(data, 'key', 'control', 'a', 3)
        update_db(data, 'value', 'control', pg.K_a, 3)

        self.update_buttons()



    def show_settings(self):
        self.run_settings = True

        image = pg.Surface((WIDTH, HEIGHT))
        pg.draw.rect(image, (75, 75, 75), (WIDTH * 0.00625, HEIGHT * 0.0125, 600, 730))
        image.set_alpha(128)

        self.update_buttons()

        while self.run_settings:
            for i in pg.event.get():
                if i.type == pg.QUIT:
                    sys.exit()
                if i.type == pg.MOUSEBUTTONDOWN:
                    self.animation_mouse_pos = pg.mouse.get_pos()
                    self.key = 1
                    self.animation_queue.append(MouseEffect(self.settings_screen, self.animation_mouse_pos))

            pg.display.set_caption(f'Space Adventure - FPS: {str(self.clock.get_fps())[:5]} - {VERSION_BUILD}')

            self.clock.tick(self.FPS)

            self.settings_screen.blit(self.bg, (0, 0))
            self.settings_screen.blit(image, (0, 0))

            for button in self.settings_buttons:
                button.draw()

            if self.key:
                for eff in self.animation_queue:
                    if not eff.alive:
                        self.animation_queue.remove(eff)
                    else:
                        eff.mouse_animation()
            self.render_text()

            pg.display.flip()


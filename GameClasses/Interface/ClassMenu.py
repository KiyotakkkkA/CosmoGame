from GameClasses.Interface.ClassGame import Game
from GameClasses.Interface.ClassInterface import Interface
from GameClasses.Interface.ClassSettings import Settings
from GameClasses.Tiles.ClassMouseEffect import MouseEffect
from GameClasses.Tiles.ClassButton import Button

from RenderedMedia import menu_space_bg, menu_animation_array

from Utility.GlobalSettings import *
from Database import *

import pygame as pg
import sys

class Menu(Interface):
    def __init__(self):
        super().__init__()

        self.menu_screen = pg.display.set_mode((WIDTH, HEIGHT))

        self.bg = pg.transform.scale(menu_space_bg, (WIDTH, HEIGHT))

        self.need_draw_click = False

    def show_settings(self):
        self.run_menu = not self.run_menu
        self.Settings = Settings()
        self.Settings.show_settings()

    def show_menu(self):
        self.run_menu = True

        # Button commands
        def run_game():
            self.run_menu = not self.run_menu
            self.Game = Game()
            self.Game.start_game()

        menu_buttons = [
            Button(self.menu_screen, WIDTH * 0.0125, HEIGHT // 2.5, ['Начать'], animation_type='rectangle', command=run_game),
            Button(self.menu_screen, WIDTH * 0.0125, HEIGHT // 2.5 + self.text_height * 1.5, ['Настройки'], animation_type='rectangle', command=self.show_settings),
            Button(self.menu_screen, WIDTH * 0.0125, HEIGHT // 2.5 + self.text_height * 3, ['Магазин'], animation_type='rectangle'),
            Button(self.menu_screen, WIDTH * 0.0125, HEIGHT - self.text_height * 4, ['Выйти'], animation_type='rectangle', command=sys.exit)
        ]

        image = pg.Surface((WIDTH, HEIGHT))
        pg.draw.rect(image, (75, 75, 75), (WIDTH * 0.00625, HEIGHT // 2.5, 290, 400))
        image.set_alpha(128)

        while self.run_menu:
            for i in pg.event.get():
                if i.type == pg.QUIT:
                    sys.exit()
                if i.type == pg.MOUSEBUTTONDOWN:
                    self.animation_mouse_pos = pg.mouse.get_pos()
                    self.key = 1
                    self.animation_queue.append(MouseEffect(self.menu_screen, self.animation_mouse_pos))

            pg.display.set_caption(f'Space Adventure - FPS: {str(self.clock.get_fps())[:5]} - {VERSION_BUILD}')

            self.clock.tick(self.FPS)

            self.menu_screen.blit(self.bg, (0, 0))
            self.menu_screen.blit(image, (0, 0))

            for button in menu_buttons:
                button.draw()

            if self.key:
                for eff in self.animation_queue:
                    if not eff.alive:
                        self.animation_queue.remove(eff)
                    else:
                        eff.mouse_animation()

            pg.display.flip()


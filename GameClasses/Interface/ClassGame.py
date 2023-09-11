import sys

from Utility.GlobalSettings import *

from GameClasses.Tiles.ClassPlayer import Player
from GameClasses.Tiles.ClassEnemy import EnemyField
from GameClasses.Tiles.ClassBullet import Bullet
from GameClasses.Tiles.ClassBonuses import AllBonuses
from GameClasses.Interface.ClassInterface import Interface
from GameClasses.Tiles.ClassButton import Button

from RenderedMedia import game_space_bg1

class Game(Interface):
    def __init__(self):
        super().__init__()
        print('sdd')

        self.screen = pg.display.set_mode((WIDTH, HEIGHT))

        self.stopped = False

        self.bg = pg.transform.scale(game_space_bg1, (WIDTH, HEIGHT))

        self.hero_bullet_array = []

    def end_game(self):
        pass

    def stop_game(self, event='stop'):

        def back():
            from main import app
            self.run_menu = not self.run_menu
            self.run = not self.run
            app.show_menu()

        def _continue():
            self.stopped = not self.stopped

        but_yes = Button(self.screen, WIDTH // 4, HEIGHT // 4, ['Да'], back, animation_type='rectangle')
        but_no = Button(self.screen, WIDTH - WIDTH // 2.5, HEIGHT // 4, ['Нет'], _continue, animation_type='rectangle')

        image = pg.Surface((WIDTH, HEIGHT))
        pg.draw.rect(image, (75, 75, 75), (0, 0, WIDTH, HEIGHT))
        image.set_alpha(3)

        self.stopped = not self.stopped

        while self.stopped and self.run:
            for i in pg.event.get():
                if i.type == pg.QUIT:
                    sys.exit()
                if i.type == pg.KEYDOWN:
                    if i.key in [pg.K_LSHIFT]:
                        self.stopped = not self.stopped

            self.screen.blit(image, (0, 0))
            if event == 'stop':
                self.many_text(self.screen, 200, HEIGHT // 8, ['Игра поставлена на паузу', 'Нажмите LSHIFT для снятия'], WHITE)
            if event == 'exit_ask':
                self.many_text(self.screen, 150, HEIGHT // 8, ['Вы действительно хотите выйти?'], WHITE)
                but_yes.draw()
                but_no.draw()
            pg.display.flip()

    def start_game(self):
        self.run = True

        # Pre-Initializing config

        player = Player()
        enemies = EnemyField(player, self.screen, 5)
        bonuses = AllBonuses(player, self.screen)

        while self.run and player.hp > 0:

            keys = pg.key.get_pressed()

            for i in pg.event.get():
                if i.type == pg.QUIT:
                    self.run = False
                if i.type == pg.KEYDOWN:

                    if i.key == pg.K_SPACE and len(self.hero_bullet_array) == 0:
                        self.hero_bullet_array.append(Bullet(player))
                    if i.key == pg.K_LSHIFT:
                        self.stop_game()
                    if i.key == pg.K_ESCAPE:
                        self.stop_game(event='exit_ask')

            self.screen.blit(self.bg, (0, 0))


            for bullet in self.hero_bullet_array:
                bullet.shot_player(self.screen)
                if bullet.check_out_player():
                    self.hero_bullet_array.remove(bullet)

            player.draw(self.screen)

            enemies.enemy_fill(self.hero_bullet_array)
            bonuses.move()

            if self.destroy_animation_queue:
                for animation in self.destroy_animation_queue:
                    animation.draw()

            if keys[self.control_dict['up'][1]]:
                player.move([True, False, False, False])
            if keys[self.control_dict['down'][1]]:
                player.move([False, True, False, False])
            if keys[self.control_dict['left'][1]]:
                player.move([False, False, True, False])
            if keys[self.control_dict['right'][1]]:
                player.move([False, False, False, True])

            pg.display.set_caption(f'Space Adventure - FPS: {str(self.clock.get_fps())[:5]} - {VERSION_BUILD}')


            self.clock.tick(self.FPS)
            pg.display.flip()


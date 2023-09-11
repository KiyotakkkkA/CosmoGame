import random as r

from Utility.GlobalSettings import *
from RenderedMedia import *
from Utility.Functions import check_collisions

from GameClasses.Debug.ClassDebuger import Debuger
from GameClasses.Interface.ClassInterface import Interface
from GameClasses.Tiles.ClassAnimation import Animation

class Enemy:
    def __init__(self, x, y, screen=None):
        super().__init__()
        self.radius = 60
        self.x = x
        self.y = y
        self.sc = screen

        self.textures_array = [pg.transform.scale(spaceship1_enemy, [self.radius, self.radius])]
        self.texture = r.choice(self.textures_array)

        self.speed_y = 2

        self.max_hp = 10
        self.hp = 10

    def draw_hp(self, sc, y):
        if self.hp != self.max_hp:
            pg.draw.rect(sc, RED, (self.x, y - 15, int(self.radius * (self.hp / self.max_hp)), 10))
            pg.draw.rect(sc, WHITE, (self.x, y - 15, self.radius, 10), 1)


    def draw(self, sc, y, colliders):
        if colliders:
            pg.draw.rect(sc, WHITE, (self.x, y, 60, 60), 1)
        self.draw_hp(sc, y)

        sc.blit(self.texture, (self.x, y))


class EnemyEscadra(Interface):
    def __init__(self, player, y, amount, x=None, sc=None):
        super().__init__()
        self.player = player
        self.sc = sc

        self.y = y
        self.speed_y = 2

        self.enemies = []
        self.amount = amount

        if x is not None:
            self.x = x
        else:
            self.x = (WIDTH - 60 * self.amount) // 2

        self.fill_array()

    def count(self):
        return len(self.enemies)

    def get_width(self):
        return self.amount * 60

    def fill_array(self):

        for i in range(self.amount):
            self.enemies.append(Enemy(self.x, self.y, screen=self.sc))
            self.x += 60

    def move_back(self):
        if self.y >= HEIGHT:
            self.y = -60

    def move(self, sc, bullet_array, colliders):
        self.move_back()

        for enemy in self.enemies:
            if enemy.hp > 0:

                enemy.draw(sc, self.y, colliders)
                if check_collisions(enemy, self.player, self.y, False):
                    self.enemies.remove(enemy)
                    self.player.hp -= 1

                for bullet in bullet_array:
                    if check_collisions(enemy, bullet, self.y, True, with_player=False):
                        bullet_array.remove(bullet)

            else:
                self.destroy_animation_queue.append(Animation(self.x, self.y))
                self.enemies.remove(enemy)

        self.y += self.speed_y
        self.x += 4


class EnemyField(Debuger):
    def __init__(self, player, sc, escadras_amount):
        super().__init__()
        self.escadras_amount = escadras_amount
        self.all_enemies = []

        self.player = player

        self.sc = sc

        self.create_enemies()

    def create_enemies(self):
        x = 10
        delta_y = 0
        for escadra in range(self.escadras_amount):
            self.all_enemies.append(EnemyEscadra(self.player, 100 + delta_y, 5, x, self.sc))
            delta_y += 60
            x = r.randint(20, WIDTH - self.all_enemies[0].get_width())

    def enemy_fill(self, hero_bullets):

        for enemy in self.all_enemies:
            if enemy.count() == 0:
                self.all_enemies.remove(enemy)
                self.all_enemies.append(EnemyEscadra(self.player, -60, 5, r.randint(20, WIDTH - self.all_enemies[0].get_width()), self.sc))

            enemy.move(self.sc, hero_bullets, self.colliders)

import random as r

from RenderedMedia import *
from Utility.Functions import check_collisions
from Utility.GlobalSettings import WIDTH, HEIGHT, WHITE, FPS
from GameClasses.Debug.ClassDebuger import Debuger

class Bonus(Debuger):
    def __init__(self, x, y, surface):
        super().__init__()
        self.x = x
        self.y = y

        self.surface = surface

        self.is_active = False

        self.speed_y = 3

        self.radius = 32

        self.image = None

    def move(self):
        self.y += self.speed_y

        if self.colliders:
            pg.draw.rect(self.surface, WHITE, (self.x, self.y, self.radius, self.radius), 1)
        self.surface.blit(self.image, (self.x, self.y))

class AddLifeBonus(Bonus):
    def __init__(self, x, y, surface):
        super().__init__(x, y, surface)

        self.image = add_heart

        self.heal = 2

    def active(self, player):
        if player.hp != player.max_hp:
            player.hp += self.heal

class SpeedBonus(Bonus):
    def __init__(self, x, y, surface):
        super().__init__(x, y, surface)

        self.image = speed_shard

        self.is_active = False

        self.duration = 3 * FPS
        self.add_speed = 3

        self.animation_counter = 0
        self.animations_array = [speed1, speed2]


    def active(self, player):
        self.is_active = True

        player.speed_y += self.add_speed
        player.speed_x += self.add_speed


    def bonus(self, player):
        self.surface.blit(pg.transform.scale(self.animations_array[int(self.animation_counter) % len(self.animations_array)],
                                   (player.radius, player.radius)), (player.x, player.y))

        self.animation_counter += 0.15
        self.duration -= 1

        if self.duration <= 0:
            player.speed_y -= self.add_speed
            player.speed_x -= self.add_speed

            self.is_active = False
            self.duration = 3 * FPS

class AllBonuses:
    def __init__(self, player, surface):
        self.player = player

        self.surface = surface

        self.life_bonuses_amount = 1
        self.speed_bonuses_amount = 1

        self.bonuses_array = []

        self.create_bonuses_array()

    def create_bonuses_array(self):
        for i0 in range(self.life_bonuses_amount):
            self.bonuses_array.append(AddLifeBonus(r.randint(WIDTH // 4, WIDTH // 4 * 3), r.randint(-10 * HEIGHT, -5 * HEIGHT),
                                                   self.surface))
        for i1 in range(self.speed_bonuses_amount):
            self.bonuses_array.append(SpeedBonus(r.randint(WIDTH // 4, WIDTH // 4 * 3), r.randint(-10 * HEIGHT, -5 * HEIGHT),
                                                 self.surface))

    def move(self):
        for bonus in self.bonuses_array:
            bonus.move()
            if check_collisions(bonus, self.player, bonus.y, False):
                bonus.active(self.player)
                bonus.y = r.randint(-HEIGHT * 10, -5 * HEIGHT)
                bonus.x = r.randint(bonus.radius, WIDTH - bonus.radius)

            if bonus.is_active:
                bonus.bonus(self.player)





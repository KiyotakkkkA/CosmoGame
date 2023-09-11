import pygame as pg

from Utility.GlobalSettings import WHITE

from RenderedMedia import bullet_array

class Bullet:
    def __init__(self, holder, class_='player'):
        if class_ == 'player':
            self.radius = 24
            self.x = holder.x + holder.radius // 2 - self.radius // 2
            self.y = holder.y

            self.speed = 4

            self.damage = 6

            self.animation_counter = 0

            self.bullet_animation = []

            for animation in bullet_array:
                self.bullet_animation.append(pg.transform.scale(animation, (self.radius, self.radius)))

    def check_out_player(self):
        if self.y + self.radius <= 0:
            return True

    def shot_player(self, sc):
        # bullet hixbox
        # pg.draw.rect(sc, WHITE, (self.x, self.y, self.radius, self.radius), 1)
        sc.blit(self.bullet_animation[int((self.animation_counter // 1) % len(self.bullet_animation))], (self.x, self.y))
        self.animation_counter += 0.5
        self.y -= self.speed

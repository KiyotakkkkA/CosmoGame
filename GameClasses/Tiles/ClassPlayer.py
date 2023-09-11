from Utility.GlobalSettings import *
from RenderedMedia import spaceship_player
from GameClasses.Debug.ClassDebuger import Debuger

class Player(Debuger):
    def __init__(self):
        super().__init__()
        self.radius = 80
        self.x = WIDTH // 2
        self.y = int(HEIGHT * 0.9) - 5

        self.score = 0

        self.texture = pg.transform.scale(spaceship_player, (self.radius, self.radius))

        self.effect_texture = None
        self.animation_counter = 0

        self.speed_y = 1
        self.speed_x = 2


        self.hp = self.max_hp = 100

    def draw_hp(self, sc):
        if self.hp < self.max_hp:
            pg.draw.rect(sc, GREEN, (self.x, self.y - 15, int(self.radius * (self.hp / self.max_hp)), 10))
            pg.draw.rect(sc, WHITE, (self.x, self.y - 15, self.radius, 10), 1)


    def draw(self, sc):
        self.draw_hp(sc)

        if self.colliders:
            pg.draw.rect(sc, WHITE, (self.x, self.y, 80, 80), 1)

        sc.blit(self.texture, (self.x, self.y))

    def move(self, direction):
        if direction[0] and self.y >= 0:
            self.y -= self.speed_y
        if direction[1] and self.y + self.radius <= HEIGHT:
            self.y += self.speed_y
        if direction[2] and self.x >= 0:
            self.x -= self.speed_x
        if direction[3] and self.x + self.radius <= WIDTH:
            self.x += self.speed_x
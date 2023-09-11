import pygame as pg

# player

spaceship_player = pg.image.load('Assets/Sprites/Player/spaceship_player.png')

bullet_array = [pg.image.load("Assets/Sprites/Bullet/bullet1.png"),
                pg.image.load("Assets/Sprites/Bullet/bullet2.png"),
                pg.image.load("Assets/Sprites/Bullet/bullet3.png"),
                pg.image.load("Assets/Sprites/Bullet/bullet4.png")]

# enemy
spaceship1_enemy = pg.image.load('Assets/Sprites/Enemy/spaceship1_enemy.png')

enemy_destroy_animation = [pg.image.load("Assets/Sprites/Enemy/destroy1.png"),
                pg.image.load("Assets/Sprites/Enemy/destroy2.png"),
                pg.image.load("Assets/Sprites/Enemy/destroy3.png"),
                pg.image.load("Assets/Sprites/Enemy/destroy4.png")]

# bonuses

add_heart = pg.image.load('Assets/Sprites/Bonuses/add_heart.png')
speed_shard = pg.image.load('Assets/Sprites/Bonuses/speed_shard.png')

# game effects

speed1 = pg.image.load('Assets/Effects/GameAnimation/speed_effect.png')
speed2 = pg.image.load('Assets/Effects/GameAnimation/speed_effect2.png')

# backgrounds

game_space_bg1 = pg.image.load('Assets/Backgrounds/Game_space_bg.jpg')
menu_space_bg = pg.image.load('Assets/Backgrounds/Menu_space_bg.jpg')

# menu effect
menu_animation_array = [pg.image.load("Assets/Effects/MenuAnimation/Light0.png"), pg.image.load(
    "Assets/Effects/MenuAnimation/Light1.png"), pg.image.load("Assets/Effects/MenuAnimation/Light2.png"),
                        pg.image.load("Assets/Effects/MenuAnimation/Light3.png"), pg.image.load(
        "Assets/Effects/MenuAnimation/Light4.png"), pg.image.load("Assets/Effects/MenuAnimation/Light5.png"),
                        pg.image.load("Assets/Effects/MenuAnimation/Light6.png"), pg.image.load(
        "Assets/Effects/MenuAnimation/Light7.png"), pg.image.load("Assets/Effects/MenuAnimation/Light8.png"),
                        pg.image.load("Assets/Effects/MenuAnimation/Light9.png"), pg.image.load(
        "Assets/Effects/MenuAnimation/Light10.png")]

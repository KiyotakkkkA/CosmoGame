import pygame as pg

class Debuger:
    def __init__(self):
        self.colliders = False

    def show_collision_boxes(self):
        self.colliders = True
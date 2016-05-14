import numpy as np
import math
import pygame as pg

class Entity:
    def __init__(self, canvas):
        self.canvas = canvas
    
    def draw(self, pos):
        pg.draw.circle(self.canvas, (200, 200, 200), np.around(pos, 0).astype(int), 20)
        
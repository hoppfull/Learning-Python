from pygamehelper import *
from pygame import *
from pygame.locals import *
from vec2d import *

import numpy as np

class Starter(PygameHelper):
    def __init__(self, width, height):
        self.w, self.h = width, height
        PygameHelper.__init__(self, size=(self.w, self.h), fill=((255,255,255)))
        
        self.unit_pos = vec2d(width/2,height/2)
        self.target_pos = vec2d(width/2,height/2)
        self.unit_img = pygame.image.load("unit1.png")
        self.target_img = pygame.image.load("target1.png")
        
    def update(self):
        pass
        
    def keyUp(self, key):
        pass
        
    def mouseUp(self, button, pos):
        self.target_pos = (pos[0], pos[1])
        
    def mouseMotion(self, buttons, pos, rel):
        pass
    
    def draw(self):
        self.screen.fill((0,0,0))
        self.screen.blit(self.target_img, (self.target_pos[0]-64, self.target_pos[1]-64))
        self.screen.blit(self.unit_img, (self.unit_pos[0]-32,self.unit_pos[1]-32))
        

s = Starter(800, 600)
s.mainLoop(40)

from pygamehelper import *
from pygame import *
from pygame.locals import *
from vec2d import *
from random import uniform

import numpy as np

class Starter(PygameHelper):
    def __init__(self):
        self.w, self.h = 800, 600
        PygameHelper.__init__(self, size=(self.w, self.h), fill=((0,0,0)))
        
    def update(self):
        pass
        
    def keyUp(self, key):
        pass
        
    def mouseUp(self, button, pos):
        pass
        
    def mouseMotion(self, buttons, pos, rel):
        pass
        
    def draw(self):
        self.screen.fill((np.random.random()*255, np.random.random()*255, np.random.random()*255))
        
s = Starter()
s.mainLoop(40)

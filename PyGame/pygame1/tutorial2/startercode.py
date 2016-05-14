from pygamehelper import *
from pygame import *
from pygame.locals import *
from vec2d import *

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
        print(buttons, pos, rel)
        if(buttons[0] == 1):
            pygame.draw.line(self.screen, (0,200,255), pos, (pos[0]-rel[0], pos[1]-rel[1]), 5)
            pygame.draw.line(self.screen, (0,200,255), (pos[0],pos[1] + 20), (pos[0]-rel[0], pos[1]-rel[1]+20), 5)
        if(buttons[2] == 1):
            pygame.draw.line(self.screen, (0,0,0), pos, (pos[0]-rel[0], pos[1]-rel[1]), 100)
        
    def draw(self):
        # self.screen.fill((0,0,0))
        pass
		
s = Starter()
s.mainLoop(40)

from pygamehelper import *
from pygame import *
from pygame.locals import *
from vec2d import *

import numpy as np

class Starter(PygameHelper):
    def __init__(self):
        self.w, self.h = 800, 600
        PygameHelper.__init__(self, size=(self.w, self.h), fill=((0,0,0)))
        
        self.img = pygame.image.load("colors.png")
        
        self.myColorSample = (0,0,0)
        self.x = 0
        
    def update(self):
        pass
        
    def keyUp(self, key):
        pass
        
    def mouseUp(self, button, pos):
        pass
        
    def mouseMotion(self, buttons, pos, rel):
        if(buttons[0] == 1):
            pygame.draw.line(self.screen, self.myColorSample, pos, (pos[0]-rel[0], pos[1]-rel[1]), 5)
        if((pos[0]<172) and(pos[1]<172) and (buttons[2] == 1)):
            self.myColorSample = self.screen.get_at(pos)
        if(buttons[1] == 1):
            #rainbow mode active!
            pygame.draw.line(self.screen, self.myColorSample, pos, (pos[0]-rel[0], pos[1]-rel[1]), 5)
            self.x = self.x + 1
            if(self.x > 171):
                self.x = 1
            
            self.myColorSample = self.screen.get_at((self.x,0))
            
        
    def draw(self):
        self.screen.blit(self.img, (0,0))
        pygame.draw.circle(self.screen, self.myColorSample, (200, 50), 20)
		
s = Starter()
s.mainLoop(40)

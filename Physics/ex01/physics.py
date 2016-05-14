import numpy as np
import math

class Physics:
    def __init__(self, entity):
        self.entity = entity
        self.pos = np.zeros(0)
        self.vel = np.zeros(0)
        self.f = np.zeros(0)
    
    def draw(self):
        for pos in self.pos:
            self.entity.draw((pos[0], pos[1]))
    
    def update(self):
        for i, p0 in enumerate(self.pos):
            for j, p1 in enumerate(self.pos):
                if(i != j):
                    print(i, j, np.linalg.norm(p0 - p1))
    
        self.vel = self.vel + self.f
        self.pos = self.pos + self.vel
        
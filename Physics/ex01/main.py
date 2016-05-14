import pygame as pg
import numpy as np
import engine
import entity
import physics

class App(engine.Engine):
    def __init__(self, size, title):
        engine.Engine.__init__(self, size, title)
        
        self.physics = physics.Physics(entity.Entity(self.canvas))
        self.physics.pos = np.array([
            [100, 100],
            [150, 300],
            [200, 100],
            [250, 150]])
        self.physics.vel = np.array([
            [0, 0],
            [0, 0],
            [0, 0],
            [0, 0]])
        self.physics.f = np.array([
            [0, 0],
            [0, 0],
            [0, 0],
            [0, 0]])
    
    def update(self):
        self.physics.update()
    
    def draw(self):
        self.physics.draw()
    
    def events(self):
        for e in pg.event.get():
            if e.type == pg.QUIT:
                self.RUNNING = False
        
        def isPressed(key):
            return pg.key.get_pressed()[ord(key)] == 1
        
if __name__ == "__main__":
    app = App((640, 480), "Physics test")
    app.run()
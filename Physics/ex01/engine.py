import pygame as pg

class Engine:
    def __init__(self, size, title):
        self.fps = 60
        pg.init()
        self.canvas = pg.display.set_mode(size)
        pg.display.set_caption(title)
        self.RUNNING = True
    
    def run(self):
        while self.RUNNING:
            self.events()
            self.update()
            self.render()
            pg.time.Clock().tick(self.fps)
        pg.quit()
        
    def render(self):
        self.canvas.fill((0,0,0))
        self.draw()
        pg.display.update()
    
    def draw(self):
        pass
    
    def update(self):
        pass
    
    def events(self):
        pass
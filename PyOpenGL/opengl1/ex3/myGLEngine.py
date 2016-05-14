import OpenGL
OpenGL.FORWARD_COMPATIBLE_ONLY = True
#Not sure if these first two lines do anything.
#They're >supposed< to give an error if we use legacy code.
#I use this since I don't know exactly what is legacy code and what isn't...
import OpenGL.GL as GL
import OpenGL.GL.shaders as GLshaders

import pygame as pg
import pygame.locals as pglocals

class GLEngine:
    def __init__(self, resolution = (400,400), maxfps = 1):
        #Here we set everything up initially.
        #This will only be executed once.
        #Variables with the self-prefix are variables that can be used by other functions
        #within this particular class. I don't know if they span across other classes but
        #that would be kinda wierd, no?
        
        pg.init()
        self.resolution, self.maxfps = resolution, maxfps
        pg.display.set_mode(self.resolution, pg.OPENGL|pg.DOUBLEBUF)
        
        self.running = True #Is the program running?
        
        #We setup the shader. I think you later compile the shader in a
        #seperate file so this won't be so cluttered
        try:
            with open("VERTEX_SHADER.txt", 'r') as fileInput: ##LOADING VERTEX_SHADER-specs FROM EXTERNAL FILE
                VERTEX_SHADER = GLshaders.compileShader(fileInput.read(), GL.GL_VERTEX_SHADER)
            del fileInput #Cleanup!
        except(GL.GLError, RuntimeError) as err:
            print("Shader compile error (VERTEX_SHADER)", err)
        
        try:
            with open("FRAGMENT_SHADER.txt", 'r') as fileInput: ##LOADING VERTEX_SHADER-specs FROM EXTERNAL FILE
                FRAGMENT_SHADER = GLshaders.compileShader(fileInput.read(), GL.GL_FRAGMENT_SHADER)
            del fileInput #Cleanup!
        except(GL.GLError, RuntimeError) as err:
            print("Shader compile error (FRAGMENT_SHADER)", err)
        
        #The shader is compiled. Remember! This only happens once!
        #So no more changes after this point!
        self.GLEngineShader = GLshaders.compileProgram(VERTEX_SHADER, FRAGMENT_SHADER)
    
    def inputEvents(self):
        #Here we handle user-input from keyboard and mouse
        for events in pg.event.get():
            if events.type == pglocals.QUIT:
                self.running = False #Program is told it's not supposed to run anymore
            if events.type == pglocals.KEYUP and events.key == pglocals.K_ESCAPE:
                self.running = False #Program is told it's not supposed to run anymore
    
    def updateScene(self):
        #Here we change things like logic, physics and properties.
        #Additionally, I believe this code should actually be executed in
        #in as much cython as possible to increase performance!
        pass
    
    def drawScene(self):
        #This is where we change graphics. Things in here won't actually be applied right away
        #to the canvas. So when this function is done, drawing will be applied right after.
        pass
    
    def mainLoop(self):
        while self.running:
            self.inputEvents()
            self.updateScene()
            self.drawScene()
            pg.display.flip() #Tells pygame to apply all changes onto its canvas
            pg.time.Clock().tick(1000/self.maxfps) #Sets how many milliseconds to pause between frames


if __name__ == "__main__":
    print("Run main.py instead!")
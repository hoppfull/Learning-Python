import OpenGL.GLUT as GLUT
import OpenGL.GL as GL

class GameEngine():
    def __init__(self, name, width, height):
        self.name = name
        self.width = width
        self.height = height
        # Setup window:
        GLUT.glutInit()
        GLUT.glutInitDisplayMode(GLUT.GLUT_RGBA | GLUT.GLUT_DOUBLE | GLUT.GLUT_DEPTH)
        GLUT.glutInitWindowSize(self.width, self.height)
        
        
        
    def setup(self): # This is access to pre mainLoop in subclass
        pass
        
    def mainLoop(self): # This is access to mainLoop in subclass
        pass
        
    def run(self):
        # Create window:
        win = GLUT.glutCreateWindow(self.name)
        
        # Setup some OpenGL settings:
        GL.glEnable(GL.GL_CULL_FACE) # This isn't enabled by default
        GL.glFrontFace(GL.GL_CCW) # Standard, right hand rule
        GL.glCullFace(GL.GL_BACK)
        
        # Subclass setup:
        self.setup()
        
        # Create update mechanism:
        GLUT.glutTimerFunc(30, self.update, 30)
        # Create redraw mechanism:
        GLUT.glutDisplayFunc(self.draw)
        
        # Create event listeners
        GLUT.glutKeyboardFunc(self.keyboardEvents)
        GLUT.glutMouseFunc(self.mouseEvents)
        GLUT.glutMotionFunc(self.motionEvents)
        
        # Start main loop:
        GLUT.glutMainLoop()
        
    def keyboardEvents(self, key, x, y):
        self.events(x, y, key=key)
        
    def mouseEvents(self, button, state, x, y):
        # The "named" inputs are passed into kwargs and stored as keys with values in a dictionary:
        self.events(x, y, button=button, state=state)
        
    def motionEvents(self, x, y):
        # These inputs are not "named" so they get passed into args as elements in a tuple:
        self.events(x, y)
        
    def events(self, *args, **kwargs):
        pass
        
    def update(self, t):
        # Schedule next update:
        GLUT.glutTimerFunc(t, self.update, t)
        # Run "GLUT.glutDisplayFunc(self.draw)":
        GLUT.glutPostRedisplay()
        
    def draw(self):
        GL.glClear(GL.GL_COLOR_BUFFER_BIT | GL.GL_DEPTH_BUFFER_BIT) # Clear window
        # Draw commands START:
        self.mainLoop()
        # Draw commands STOP!
        GLUT.glutSwapBuffers() # Apply render to screen
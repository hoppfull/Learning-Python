import OpenGL.GLUT as GLUT
import sys

class Window():
    def __init__(self):
        GLUT.glutInit(sys.argv)
        GLUT.glutInitDisplayMode(GLUT.GLUT_RGBA | GLUT.GLUT_DOUBLE | GLUT.GLUT_DEPTH)
        GLUT.glutInitWindowSize(640, 480)
        self.win = GLUT.glutCreateWindow("PyOpenGL!!")
        
        # "glutTimerFunc" takes in three arguments
        GLUT.glutTimerFunc(
            20, # how long to wait
            self.update, # when initial wait, run this function
            20) # pass this value as argument to function
        
        # Called every frame:
        GLUT.glutDisplayFunc(self.draw)
        # application main loop:
        GLUT.glutMainLoop()
        
        
        
        
    def update(self, t):
        # Schedule another execution of this update function:
        GLUT.glutTimerFunc(t, self.update, t)
        # Execute "glutDisplayFunc()"
        GLUT.glutPostRedisplay()
        print "yo!"
        
    def draw(self):
        print "drawing!"
        
if __name__ == "__main__":
    w = Window()
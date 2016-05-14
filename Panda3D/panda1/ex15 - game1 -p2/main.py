import direct.showbase.ShowBase as p3d_SB
import Scene, Fighter

class MyApp(p3d_SB.ShowBase):
    def __init__(self):
        p3d_SB.ShowBase.__init__(self)
        
        render.setShaderAuto()
        base.disableMouse()
        
        myscene = Scene.Scene()
        myscene.setupScene()
        
        myfighter = Fighter.Fighter()
        myfighter.spawnFighter()
        
        taskMgr.doMethodLater(0, myfighter.controlFighter, 'controlFighter1')
        
if __name__ == "__main__":
    myapp = MyApp()
    myapp.run()
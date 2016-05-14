import MyPads360
import direct.showbase.ShowBase as p3d_SB

class MyApp(p3d_SB.ShowBase):
    def __init__(self):
        p3d_SB.ShowBase.__init__(self)
        self.mypads = MyPads360.MyPads360()
        
        self.render.setShaderAuto()
        #Disable mouse control over camera so we can control it with code:
        base.disableMouse()
        self.setupScene()
        self.setupPlayer()
        
    def setupPlayer(self):
        self.fighter_np = loader.loadModel("res/models/fighter")
        self.fighter_np.setScale(0.1, 0.1, 0.1)
        self.fighter_np.setPos(0, -5, 0.3)
        self.fighter_np.reparentTo(self.render)
    
    def setupScene(self):
        self.env_np = loader.loadModel("res/models/environment")
        self.env_np.reparentTo(self.render)
        
        self.sphere_np = loader.loadModel("res/models/sphere")
        self.sphere_np.reparentTo(self.render)
        
        self.camera.setPos(0, -15, 10)
        self.camera.setHpr(0, -35, 0)
        
        dlight1 = p3d_SB.DirectionalLight("Main light source")
        dlight1.setColor((1, 0.98, 0.93, 1))
        dlight1_np = self.render.attachNewNode(dlight1)
        dlight1_np.setPos(3, -1, 4)
        dlight1_np.lookAt(self.render)
        self.render.setLight(dlight1_np)
        
if __name__ == "__main__":
    app = MyApp()
    app.run()
import direct.showbase.ShowBase as p3d_SB

class Scene():
    def __init__(self):
        pass
        
    def setupScene(self):
        self.env_np = loader.loadModel("res/models/environment")
        self.env_np.reparentTo(render)
        
        self.dlight1 = p3d_SB.DirectionalLight("Main light source")
        self.dlight1.setColor((1, 0.97, 0.92, 1))
        self.dlight1_np = render.attachNewNode(self.dlight1)
        self.dlight1_np.setPos(1, -3, 4)
        self.dlight1_np.lookAt(render)
        render.setLight(self.dlight1_np)
        
        camera.setPos(0, -15, 10)
        camera.setHpr(0, -35, 0)
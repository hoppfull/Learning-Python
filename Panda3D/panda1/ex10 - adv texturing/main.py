import direct.showbase.ShowBase as p3d_SB
import panda3d.core as p3d_Core

class MyApp(p3d_SB.ShowBase):
    def __init__(self):
        p3d_SB.ShowBase.__init__(self)

        light = p3d_SB.PointLight("Main Light")
        light_nodepath = render.attachNewNode(light)
        light_nodepath.setPos(0,5,3)
        render.setLight(light_nodepath)

        model = loader.loadModel("res/models/stargate.bam")
        model.reparentTo(self.render)
        
        self.render.setShaderAuto()

if __name__ == "__main__":
    app = MyApp()
    app.run()

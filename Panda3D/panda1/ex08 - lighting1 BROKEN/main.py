import direct.showbase.ShowBase as p3d_SB
import panda3d.core as p3d_Core

class MyApp(p3d_SB.ShowBase):
    def __init__(self):
        p3d_SB.ShowBase.__init__(self)

        self.icosphere = self.loader.loadModel("res/models/icosphere") #Load model
        self.icosphere.reparentTo(self.render)  #Parent model under render in the scene graph

        self.dlight_main = p3d_Core.DirectionalLight("Main light")
        self.dlight_main.setColor(p3d_Core.VBase4(1,0,0,1))
        self.dlnp = self.render.attachNewNode(self.dlight_main)
        self.dlnp.setHpr(0, -60, 0)
        self.render.setLight(self.dlnp)

        #Note: The object is actually shaded but the directional light source is acting wierd.
	#Note: Try a point light instead and shading will be obvious

if __name__ == "__main__":
    app = MyApp()
    app.run()

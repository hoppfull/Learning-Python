import direct.showbase.ShowBase as p3d_SB
import panda3d.core as p3d_Core

#Nothing in here needs to be done in order to work with texturing
#Panda deals with this stuff for us. The .egg-files needs work though.

class MyApp(p3d_SB.ShowBase):
    def __init__(self):
        p3d_SB.ShowBase.__init__(self)
        
        mesh_np = loader.loadModel("res/environment")
        mesh_np.reparentTo(render)
        mesh_np.set_shader( p3d_Core.Shader.load(p3d_Core.Shader.SL_GLSL, "vertexshader.glsl", "fragmentshader.glsl") )
        
if __name__ == "__main__":
    myapp = MyApp()
    myapp.run()
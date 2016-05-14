import direct.showbase.ShowBase as p3d_SB
import panda3d.core as p3d_Core

##This requires Panda3D-2014.11.27-503 (dev-version) to work properly!

class MyApp(p3d_SB.ShowBase):
    def __init__(self):
        p3d_SB.ShowBase.__init__(self)
        
        mesh_np = loader.loadModel("pyramid")
        mesh_np.reparentTo(render)
        mesh_np.set_shader( p3d_Core.Shader.load(p3d_Core.Shader.SL_GLSL, "vertexshader.glsl", "fragmentshader.glsl") )
        
if __name__ == '__main__':
    myapp = MyApp()
    myapp.run()
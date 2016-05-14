import direct.showbase.ShowBase as p3d_SB
import panda3d.core as p3d_Core

class MyApp(p3d_SB.ShowBase):
    def __init__(self):
        p3d_SB.ShowBase.__init__(self)
        
        self.mesh_np = loader.loadModel("res/stargate01")
        self.mesh_np.reparentTo(render)
        self.mesh_np.set_shader( p3d_Core.Shader.load(p3d_Core.Shader.SL_GLSL, "vertexshader.glsl", "fragmentshader.glsl") )
        self.mesh_np.set_shader_input('DiffusionCM01', loader.loadCubeMap("res/DiffusionCM01.txo"))
        self.mesh_np.set_shader_input('Spec128CM01', loader.loadCubeMap("res/Spec128CM01.txo"))

if __name__ == "__main__":
    myapp = MyApp()
    myapp.run()
import direct.showbase.ShowBase as p3d_SB
import panda3d.core as p3d_Core

class MyApp(p3d_SB.ShowBase):
    def __init__(self):
        p3d_SB.ShowBase.__init__(self)
        
        mesh_np = loader.loadModel("res/pyramid")
        mesh_np.reparentTo(render)
        mesh_np.set_shader( p3d_Core.Shader.load(p3d_Core.Shader.SL_GLSL, "vertexshader.glsl", "fragmentshader.glsl") )
        
        #Pass a variable to the shader program:
        mesh_np.set_shader_input('x', 1.0)
        
        #If the variable isn't used by the shader, no problems will occur.
        
if __name__ == "__main__":
    myapp = MyApp()
    myapp.run()
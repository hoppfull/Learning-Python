import direct.showbase.ShowBase as p3d_SB
import panda3d.core as p3d_Core

## Make sure High Performance GPU is preferred!
## My integrated INTEL video card cannot do compute shaders!

class MyApp(p3d_SB.ShowBase):
    def __init__(self):
        p3d_SB.ShowBase.__init__(self)
        
        computeshader_node = p3d_Core.ComputeNode('computeshader')
        computeshader_node.add_dispatch(512/16, 512/16, 1)
        computeshader_np = render.attachNewNode(computeshader_node)
        computeshader_np.setShader( p3d_Core.Shader.loadCompute(p3d_Core.Shader.SL_GLSL, "computeshader.glsl") )
        
        
        
        
        
if __name__ == "__main__":
    myapp = MyApp()
    myapp.run()
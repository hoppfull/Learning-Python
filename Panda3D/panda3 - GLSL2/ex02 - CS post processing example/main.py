import direct.showbase.ShowBase as p3d_SB
import panda3d.core as p3d_Core

class MyApp(p3d_SB.ShowBase):
    def __init__(self):
        p3d_SB.ShowBase.__init__(self)
        
        computeshader_node = p3d_Core.ComputeNode('computeshader_node')
        # We dispatch a "Global Work Group" of a number of "Local Work Groups":
        computeshader_node.add_dispatch(16, 16, 1) # Global Work Group = 16*16*1=256 Local Work Groups
        computeshader_np = render.attachNewNode(computeshader_node)
        computeshader_np.setShader( p3d_Core.Shader.loadCompute(p3d_Core.Shader.SL_GLSL, "computeshader.glsl") )
        
        tex_in = loader.loadTexture("res/tex1.png")
        tex_in.set_format(p3d_Core.Texture.F_rgba32)
        tex_out = loader.loadTexture("res/tex2.png")
        tex_out.set_format(p3d_Core.Texture.F_rgba8)
        
        computeshader_np.set_shader_input('tex_in', tex_in)
        computeshader_np.set_shader_input('tex_out', tex_out)
        
        cm = p3d_Core.CardMaker('card')
        card = render2d.attachNewNode(cm.generate())
        card.setScale(2.0)
        card.setPos(-1, 0, -1)
        card.setTexture(tex_out)
        
if __name__ == "__main__":
    myapp = MyApp()
    myapp.run()
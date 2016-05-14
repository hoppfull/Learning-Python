import direct.showbase.ShowBase as p3d_SB
import panda3d.core as p3d_Core

class MyApp(p3d_SB.ShowBase):
    def __init__(self):
        p3d_SB.ShowBase.__init__(self)
        
        self.mesh_np = loader.loadModel("res/cube")
        self.mesh_np.reparentTo(render)
        self.mesh_np.set_shader( p3d_Core.Shader.load(p3d_Core.Shader.SL_GLSL, "vertexshader.glsl", "fs_phong.glsl") )
        #If a directional light always pointed to the center, where would it be located?
        self.mesh_np.set_shader_input('dlight1_pos', (0.0, -1.0, -1.0, 1.0))
        self.mesh_np.set_shader_input('dlight1_col', (0.8, 0.8, 0.8))
        self.mesh_np.set_shader_input('Ambience', (0.03, 0.03, 0.03))
        
        taskMgr.doMethodLater(0, self.rotate, 'rotate')
        
    def rotate(self, task):
        self.mesh_np.setHpr( self.mesh_np.getH() + 1.0, self.mesh_np.getP() + 0.0,  self.mesh_np.getR() + 0.0)
        return task.again
        
if __name__ == "__main__":
    myapp = MyApp()
    myapp.run()
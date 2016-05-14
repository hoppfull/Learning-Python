import direct.showbase.ShowBase as p3d_SB
import panda3d.core as p3d_Core

class MyApp(p3d_SB.ShowBase):
    def __init__(self):
        p3d_SB.ShowBase.__init__(self)
        
        self.mesh_np = loader.loadModel("res/stargate")
        self.mesh_np.reparentTo(render)
        self.mesh_np.set_shader( p3d_Core.Shader.load(p3d_Core.Shader.SL_GLSL, "vertexshader.glsl", "fragmentshader.glsl") )
        
        taskMgr.doMethodLater(0, self.rotate, 'rotate')
        
    def rotate(self, task):
        self.mesh_np.setHpr(0.0, 0.0, self.mesh_np.getR() + 0.3)
        return task.again
        
if __name__ == "__main__":
    myapp = MyApp()
    myapp.run()
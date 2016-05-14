import direct.showbase.ShowBase as p3d_SB
import panda3d.core as p3d_Core

class MyApp(p3d_SB.ShowBase):
    def __init__(self):
        p3d_SB.ShowBase.__init__(self)
        base.disableMouse()
        
        mybuffer = base.win.makeTextureBuffer('mybuffer', 512, 512)
        mybuffer.setSort(-1)
        mybuffer.setClearColor((0.0, 0.0, 0.0, 1.0))
        
        mycamera = base.makeCamera(mybuffer, lens=base.cam.node().getLens())
        myscene = p3d_Core.NodePath('myscene')
        mycamera.reparentTo(myscene)
        mycamera.setPos(0.0, -5.0, 0.0)
        
        self.mesh_np = loader.loadModel("res/icosphere")
        self.mesh_np.reparentTo(myscene)
        taskMgr.doMethodLater(0, self.rotate, 'rotate')
        
        card = mybuffer.getTextureCard()
        card.reparentTo(render2d)
        card.set_shader( p3d_Core.Shader.load(p3d_Core.Shader.SL_GLSL, "vs.glsl", "fs.glsl") )
        
        
        
        
        
        # buffer viewer (debugging):
        self.accept("v", base.bufferViewer.toggleEnable)
        base.bufferViewer.setPosition("llcorner")
        base.bufferViewer.setCardSize(0.652,0)
        
    def rotate(self, task):
        self.mesh_np.setH(self.mesh_np.getH() + 1)
        return task.again
        
if __name__ == "__main__":
    myapp = MyApp()
    myapp.run()
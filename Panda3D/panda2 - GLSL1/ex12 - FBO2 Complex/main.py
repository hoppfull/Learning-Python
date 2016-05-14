import direct.showbase.ShowBase as p3d_SB
import panda3d.core as p3d_Core

class MyApp(p3d_SB.ShowBase):
    def __init__(self):
        p3d_SB.ShowBase.__init__(self)
        base.disableMouse() # Disable mouse listener, no need for it
        base.cam.node().setActive(0) # Disable main camera, no need for it
        
        fbProps = p3d_Core.FrameBufferProperties()
        fbProps.setRgbColor(1)
        fbProps.setAlphaBits(1)
        fbProps.setDepthBits(1)
        winProps = p3d_Core.WindowProperties()
        FBO = base.graphicsEngine.makeOutput(
            base.pipe, 'myFBO', -2,
            fbProps, winProps,
            p3d_Core.GraphicsPipe.BFSizeTrackHost | p3d_Core.GraphicsPipe.BFRefuseWindow,
            base.win.getGsg(), base.win) ## This last argument produces the error when closing program.
        
        FBO.setSort(-1)
        FBO.setClearColor((0.0, 0.0, 0.0, 1.0))
        
        texDepth = p3d_Core.Texture()
        texDepth.setFormat(p3d_Core.Texture.FDepthStencil)
        texColor = p3d_Core.Texture()
        
        FBO.addRenderTexture(texDepth, p3d_Core.GraphicsOutput.RTMBindOrCopy, p3d_Core.GraphicsOutput.RTPDepthStencil)
        FBO.addRenderTexture(texColor, p3d_Core.GraphicsOutput.RTMBindOrCopy, p3d_Core.GraphicsOutput.RTPColor)
        
        camFBO = base.makeCamera(FBO, lens=base.cam.node().getLens())
        sceneFBO = p3d_Core.NodePath('sceneFBO')
        camFBO.reparentTo(sceneFBO)
        camFBO.setPos(0.0, -5.0, 0.0)
        
        self.mesh_np = loader.loadModel("res/icosphere")
        self.mesh_np.reparentTo(sceneFBO)
        taskMgr.doMethodLater(0, self.rotate, 'rotate')
        
        cardFBO = FBO.getTextureCard()
        cardFBO.reparentTo(render2d)
        camFBO.set_shader( p3d_Core.Shader.load(p3d_Core.Shader.SL_GLSL, "vs.glsl", "fs.glsl") )
        
		
        
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
    
## Look inside Tut-Fireflies.py for more on deferred shading!
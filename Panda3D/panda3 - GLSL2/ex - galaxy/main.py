import direct.showbase.ShowBase as p3d_SB
import panda3d.core as p3d_Core
import direct.interval.LerpInterval as p3d_Lerp
import direct.filter.FilterManager as p3d_FM

class LensApp(p3d_SB.ShowBase):
	def __init__(self):
		p3d_SB.ShowBase.__init__(self)
		
		base.cam.node().setActive(1) # Disable main camera rendering, no need for it
		base.setBackgroundColor(0,0,0,1)
		self.setupBFStructure() # Foreground-Background Structure
		self.setupGalaxy()
	
	def setupGalaxy(self):
		self.galaxy_np = loader.loadModel("res/models/galaxy")
		self.galaxy_np.reparentTo(self.background_np)
		self.galaxy_np.setPos(0, 3, 0)
		self.galaxy_np.setHpr(0, 60, 30)
		self.galaxy_np.set_shader(p3d_Core.Shader.load(
			p3d_Core.Shader.SL_GLSL,
			"res/shaders/vs_galaxy.glsl",
			"res/shaders/fs_galaxy.glsl"))
		interval = p3d_Lerp.LerpFunc(self.twirlDisc,
			fromData=0,
			toData=1,
			duration=30.0)
		
		interval.start()
		interval.loop()
	
	def twirlDisc(self, t):
		self.galaxy_np.set_shader_input('turn', t)
	
	def setupBFStructure(self): # Foreground-Background Structure
		self.foreground_np = render.attachNewNode('Foreground stuff')
		self.background_np = render.attachNewNode('Background stuff')
		
		# This pattern makes everything in background_np be rendered
		# behind everything else, no matter their relative positions:
		self.background_np.set_bin("background", 0)
		self.background_np.set_depth_write(False)
		
		self.foreground_np.reparentTo(render) # Everything in foreground_np will be parented to the scene
		self.background_np.reparentTo(camera) # Everything in background_np will be parented to the camera
		self.background_np.set_compass() # Everything in background_np will always face the same direction
		
if __name__ == "__main__":
	app = LensApp()
	app.run()
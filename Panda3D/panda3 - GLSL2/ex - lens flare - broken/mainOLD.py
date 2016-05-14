import direct.showbase.ShowBase as p3d_SB
import panda3d.core as p3d_Core
import direct.interval.LerpInterval as p3d_Lerp
import direct.filter.FilterManager as p3d_FM

class LensApp(p3d_SB.ShowBase):
	def __init__(self):
		p3d_SB.ShowBase.__init__(self)
		
		base.cam.node().setActive(0) # Disable main camera rendering, no need for it
		self.setupBFStructure() # Foreground-Background Structure
		self.setupGalaxy()
		
		# A buffer to hold main render:
		hires_FBO = base.win.makeTextureBuffer('hires_FBO', base.win.getXSize(), base.win.getYSize())
		# A buffer to hold the downsample of main render:
		lores_FBO = base.win.makeTextureBuffer('lores_FBO', 64, 64)
		
		# Setup render order:
		hires_FBO.setSort(-2)
		lores_FBO.setSort(-1)
		
		# Main render background is set to black:
		hires_FBO.setClearColor((0,0,0,1))
		# Downsample background is set to yellow, it wont show unless something is wrong:
		lores_FBO.setClearColor((1,1,0,1))
		
		# Create main render camera and copy properties from default camera:
		hires_cam = base.makeCamera(hires_FBO, lens=base.cam.node().getLens())
		# Create downsample camera and copy properties from default camera2d:
		lores_cam = base.makeCamera(lores_FBO, lens=base.cam2d.node().getLens())
		
		# Parent main render to default camera to utilize it's mouse listener:
		hires_cam.reparentTo(camera)
		# Get a pointer to main render output:
		hires_output = hires_FBO.getTexture()
		
		# Create new scene outside scene graph:
		filter_scene = p3d_Core.NodePath('filter_scene')
		# Parent the downsample camera to our newly created and isolated scene graph:
		lores_cam.reparentTo(filter_scene)
		# Create a canvas and parent it to our newly created and isolated scene graph:
		##filter_canvas = filter_scene.attachNewNode(p3d_Core.CardMaker('filter_canvas').generate())
		filter_canvas = loader.loadModel("res/models/canvas")
		filter_canvas.reparentTo(filter_scene)
		tex_lens_weight = loader.loadTexture("res/textures/lens_weight.jpg")
		
		# Assign lens filter shader to downsampled scene:
		filter_canvas.set_shader(p3d_Core.Shader.load(
			p3d_Core.Shader.SL_GLSL,
			"res/shaders/vs_filter.glsl",
			"res/shaders/fs_filter.glsl"))
		filter_canvas.set_shader_input('hires_output', hires_output)
		filter_canvas.set_shader_input('lens_weight', tex_lens_weight)
		filter_canvas.set_shader_input('win_size', (base.win.getXSize(), base.win.getYSize()))
		filter_canvas.set_shader_input('buffer_size', (hires_output.getXSize(), hires_output.getYSize()))
		# Get a pointer to downsampled lens filter output:
		lores_output = lores_FBO.getTexture()
		
		# Create a canvas and parent it to the render2d-scene graph to be showed on screen:
		canvas = render2d.attachNewNode(p3d_Core.CardMaker('canvas').generate())
		
		tex_vignette = loader.loadTexture("res/textures/vignette.jpg")
		
		# Assign composition shader to composite lens effect with main render:
		canvas.set_shader(p3d_Core.Shader.load(
			p3d_Core.Shader.SL_GLSL,
			"res/shaders/vs_canvas.glsl",
			"res/shaders/fs_canvas.glsl"))
		canvas.set_shader_input('hires_output', hires_output)
		canvas.set_shader_input('lores_output', lores_output)
		canvas.set_shader_input('vignette', tex_vignette)
		canvas.set_shader_input('win_size', (base.win.getXSize(), base.win.getYSize()))
		canvas.set_shader_input('buffer_size', (hires_output.getXSize(), hires_output.getYSize()))
	
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
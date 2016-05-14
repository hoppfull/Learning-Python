import direct.showbase.ShowBase as p3d_SB
import panda3d.core as p3d_Core
import direct.interval.LerpInterval as p3d_Lerp
import math
import ctypes as c

class LensApp(p3d_SB.ShowBase):
	def __init__(self):
		p3d_SB.ShowBase.__init__(self)
		
		base.cam.node().setActive(0) # Disable main camera rendering, no need for it
		self.setupBFStructure() # Foreground-Background Structure
		self.setupGalaxy()
		
		lores_buffer_p = self.setupLoresRender()
		lores_buffer_p.set_format(p3d_Core.Texture.F_rgba32)
		hires_buffer_p = self.setupHiresRender()
		
		
		cs_filter_n = p3d_Core.ComputeNode('cs_filter_n')
		# We dispatch a "Global Work Group" of a number of "Local Work Groups":
		cs_filter_n.add_dispatch(256, 1, 1) # Global Work Group = 256*1*1=256 Local Work Groups
		cs_filter_np = render.attachNewNode(cs_filter_n)
		cs_filter_np.set_shader( p3d_Core.Shader.loadCompute(p3d_Core.Shader.SL_GLSL, "res/shaders/cs_filter.glsl") )
		
		temp1_buffer = base.win.makeTextureBuffer('temp1_buffer', 256, 256)
		temp2_buffer = base.win.makeTextureBuffer('temp2_buffer', 256, 256)
		# Looks like we have to set sorting even if we don't render to these buffers:
		temp1_buffer.setSort(1)
		temp2_buffer.setSort(2)
		
		temp1_buffer_p = temp1_buffer.getTexture()
		temp1_buffer_p.set_format(p3d_Core.Texture.F_rgba32)
		temp2_buffer_p = temp2_buffer.getTexture()
		temp2_buffer_p.set_format(p3d_Core.Texture.F_rgba32)
		
		cs_filter_np.set_shader_input('lores_buffer_p', lores_buffer_p)
		cs_filter_np.set_shader_input('temp1_buffer_p', temp1_buffer_p)
		cs_filter_np.set_shader_input('temp2_buffer_p', temp2_buffer_p)
		
		
		# canvas = loader.loadModel("res/models/canvas")
		# canvas.reparentTo(render2d)
		
		
		# buffer viewer (debugging):
		self.accept("v", base.bufferViewer.toggleEnable)
		base.bufferViewer.setLayout('vgrid')
		base.bufferViewer.setPosition('llcorner')
		base.bufferViewer.setCardSize(0.98,0.98)
	
	def setupHiresRender(self): # Here we render the main scene:
		hires_buffer = base.win.makeTextureBuffer('hires_buffer', base.win.getXSize(), base.win.getYSize())
		hires_buffer.setSort(-2)
		hires_buffer.setClearColor((1, 0, 0, 1))
		hires_camera = base.makeCamera(hires_buffer, lens=base.cam.node().getLens())
		hires_camera.reparentTo(camera)
		return hires_buffer.getTexture()
	
	def setupLoresRender(self): # Here we render the main resource for lens effect:
		lores_buffer = base.win.makeTextureBuffer('lores_buffer', 256, 256)
		lores_buffer.setSort(-1)
		lores_buffer.setClearColor((1, 1, 0, 1))
		lens = p3d_Core.PerspectiveLens()
		lens.setFov(80)
		lores_camera = base.makeCamera(lores_buffer, lens=lens)
		lores_camera.reparentTo(camera)
		return lores_buffer.getTexture()
	
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
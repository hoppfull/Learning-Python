import direct.showbase.ShowBase as p3d_SB
import direct.filter.FilterManager as p3d_FM
import panda3d.core as p3d_Core

class MyApp(p3d_SB.ShowBase):
	def __init__(self):
		p3d_SB.ShowBase.__init__(self)
		base.setBackgroundColor(0,0,0)
		
		# Setup scene:
		asteroids_np = loader.loadModel("res/models/asteroids")
		asteroids_np.reparentTo(render)
		
		# FilterManager:
		fltr_mgr = p3d_FM.FilterManager(base.win, base.cam)
		tex_render = p3d_Core.Texture()
		tex_vgauss = p3d_Core.Texture()
		tex_hgauss = p3d_Core.Texture()
		
		
		# Generate a screen quad and render scene into tex_render:
		canvas_np = fltr_mgr.renderSceneInto(colortex=tex_render)
		
		# Generate a screen quad and render it into tex_vgauss (downsampled by a factor of 4):
		quad_stage1_np = fltr_mgr.renderQuadInto(colortex=tex_vgauss, div=4)
		# Apply vertical gaussian filter to tex_render:
		quad_stage1_np.set_shader(p3d_Core.Shader.load(
			p3d_Core.Shader.SL_GLSL, "res/shaders/vs_vgauss.glsl", "res/shaders/fs_vgauss.glsl"))
		quad_stage1_np.set_shader_input('tex_render', tex_render)
		
		# Generate a screen quad and render it into tex_hgauss (downsampled by a factor of 4):
		quad_stage1_np = fltr_mgr.renderQuadInto(colortex=tex_hgauss, div=4)
		# Apply horizontal gaussian filter to tex_vgauss:
		quad_stage1_np.set_shader(p3d_Core.Shader.load(
			p3d_Core.Shader.SL_GLSL, "res/shaders/vs_hgauss.glsl", "res/shaders/fs_hgauss.glsl"))
		quad_stage1_np.set_shader_input('tex_vgauss', tex_vgauss)
		
		
		canvas_np.set_shader(p3d_Core.Shader.load(
			p3d_Core.Shader.SL_GLSL, "res/shaders/vs_composition.glsl", "res/shaders/fs_composition.glsl"))
		canvas_np.set_shader_input('tex_render', tex_render)
		canvas_np.set_shader_input('whatevs', tex_hgauss)
		
		
		
		
if __name__ == "__main__":
	app = MyApp()
	app.run()
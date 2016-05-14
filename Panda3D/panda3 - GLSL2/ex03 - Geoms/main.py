import direct.showbase.ShowBase as p3d_SB
import panda3d.core as p3d_Core

class MyApp(p3d_SB.ShowBase):
	def __init__(self):
		p3d_SB.ShowBase.__init__(self)
		
		# Define a new GeomVertexFormat:
		vertex_array = p3d_Core.GeomVertexArrayFormat()
		vertex_array.addColumn(
			p3d_Core.InternalName.make('vertex'), 3,
			p3d_Core.Geom.NTFloat32, p3d_Core.Geom.COther)
		vertex_array.addColumn(
			p3d_Core.InternalName.make('hello'), 3,
			p3d_Core.Geom.NTFloat32, p3d_Core.Geom.COther)
		
		"""Turns out you need atleast >one< column named 'vertex'
		for the shader to be even called. Without the 'vertex'-name
		nothing happens. Shader doesn't seem to even compile. But add
		that name and any other name you like, and it works perfect!
		"""
		
		# Register the new GeomVertexFormat:
		format = p3d_Core.GeomVertexFormat()
		format.addArray(vertex_array)
		format = p3d_Core.GeomVertexFormat.registerFormat(format)
		
		# Define new GeomVertexData:
		vertex_data = p3d_Core.GeomVertexData('vertex_data', format, p3d_Core.Geom.UHStatic)
		vertex_data.setNumRows(3)
		
		# Create GeomVertexWriter for each column of vertex data:
		pos = p3d_Core.GeomVertexWriter(vertex_data, 'vertex')
		vel = p3d_Core.GeomVertexWriter(vertex_data, 'hello')
		
		# Add data to "vertex_data":
		pos.addData3f( 0.0, 1.0, 0.0)
		vel.addData3f( 0.0, 0.0, 1.0)
		
		pos.addData3f(-1.0,-1.0, 0.0)
		vel.addData3f(-1.0, 0.0,-1.0)
		
		pos.addData3f( 1.0,-1.0, 0.0)
		vel.addData3f( 1.0, 0.0,-1.0)
		
		# Create GeomPrimitive:
		prim = p3d_Core.GeomTriangles(p3d_Core.Geom.UHStatic)
		prim.addVertex(0)
		prim.addVertex(1)
		prim.addVertex(2)
		
		
		# Create Geom:
		geom = p3d_Core.Geom(vertex_data)
		geom.addPrimitive(prim)
		node = p3d_Core.GeomNode('whatevs')
		node.addGeom(geom)
		
		nodePath = render.attachNewNode(node)
		nodePath.set_shader( p3d_Core.Shader.load(p3d_Core.Shader.SL_GLSL, "vs.glsl", "fs.glsl") )
		
if __name__ == "__main__":
	myapp = MyApp()
	myapp.run()
import direct.showbase.ShowBase as p3d_SB

class MyApp(p3d_SB.ShowBase):
    def __init__(self):
        p3d_SB.ShowBase.__init__(self)
        render.setShaderAuto()

        foreground_np = render.attachNewNode("Foreground stuff") # This nodepath handles all things near
        background_np = render.attachNewNode("Background stuff") # This nodepath handle all things far away

        # This pattern makes everything in background_np be rendered
        # behind everything else, no matter their relative positions:
        background_np.set_bin("background", 0)
        background_np.set_depth_write(False)

        foreground_np.reparentTo(render) # Everything in foreground_np will be parented to the scene
        background_np.reparentTo(camera) # Everything in background_np will be parented to the camera
        background_np.set_compass() # Everything in background_np will always face the same direction

        torus_np = loader.loadModel("models/torus")
        icosphere_np = loader.loadModel("models/icosphere")

        torus_np.reparentTo(foreground_np)
        icosphere_np.reparentTo(background_np)
        icosphere_np.setPos(0, 5, 0)

        dlight1 = p3d_SB.DirectionalLight("Main light source")
        dlight1.setColor((1, 0.9, 0.7, 1)) # Dry sandy color
        dlight1_np = render.attachNewNode(dlight1)
        dlight1_np.setPos(5, -2, 3)
        dlight1_np.lookAt(render)
        foreground_np.setLight(dlight1_np)

if __name__ == "__main__":
    app = MyApp()
    app.run()

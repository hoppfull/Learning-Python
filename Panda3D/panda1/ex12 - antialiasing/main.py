import direct.showbase.ShowBase as p3d_SB

class MyApp(p3d_SB.ShowBase):
    def __init__(self):
        p3d_SB.ShowBase.__init__(self)
        render.setShaderAuto()
        render.setAntialias(p3d_SB.AntialiasAttrib.MAuto) #This is basicly it
        
        # For this to work one has to add the lines:
        # 'framebuffer-multisample 1
        # multisamples 2'
        # to the Config.prc file in the Panda3D SDK, located in /etc
        

        model_nodepath = loader.loadModel("model/stargate.bam")
        model_nodepath.reparentTo(render)

        dlight1 = p3d_SB.DirectionalLight("Main light source")
        dlight1.setColor((1, 1, 0.95, 1)) #Bright white
        dlight1_nodepath = render.attachNewNode(dlight1)
        dlight1_nodepath.setPos(0, -1, 5) #Position
        dlight1_nodepath.lookAt(render)
        render.setLight(dlight1_nodepath)

        dlight2 = p3d_SB.DirectionalLight("Back light source")
        dlight2.setColor((0.22, 0.25, 0.35, 1)) #Dim blue
        dlight2_nodepath = render.attachNewNode(dlight2)
        dlight2_nodepath.setPos(1, 3, -1) #Position
        dlight2_nodepath.lookAt(render)
        render.setLight(dlight2_nodepath)

        alight3 = p3d_SB.AmbientLight("Ambient light source")
        alight3.setColor((0.15, 0.12, 0.05, 1)) #Dim warm yellow
        alight3_nodepath = render.attachNewNode(alight3)
        render.setLight(alight3_nodepath)

        


if __name__ == '__main__':
    app = MyApp()
    app.run()

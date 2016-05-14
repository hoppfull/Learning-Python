import direct.showbase.ShowBase as p3d_SB


class MyApp(p3d_SB.ShowBase):
    def __init__(self):
        p3d_SB.ShowBase.__init__(self)
        render.setShaderAuto()
        
        dlight1 = p3d_SB.DirectionalLight("Main light")
        dlight1.setColor((1, 1, 0.95, 1))
        dlight1_nodepath = render.attachNewNode(dlight1)
        dlight1_nodepath.setPos(0, -5, 2)
        dlight1_nodepath.lookAt(render)
        render.setLight(dlight1_nodepath)

        dlight2 = p3d_SB.DirectionalLight("Back light")
        dlight2.setColor((0.22, 0.25, 0.35, 1))
        dlight2_nodepath = render.attachNewNode(dlight2)
        dlight2_nodepath.setPos(1, 3, -1)
        dlight2_nodepath.lookAt(render)
        render.setLight(dlight2_nodepath)

        alight3 = p3d_SB.AmbientLight("Ambient light")
        alight3.setColor((0.15, 0.12, 0.05, 1))
        alight3_nodepath = render.attachNewNode(alight3)
        render.setLight(alight3_nodepath)

        stargate_nodepath = loader.loadModel("res/models/stargate/stargate.bam")
        stargate_nodepath.reparentTo(render)
        

if __name__ == "__main__":
    app = MyApp()
    app.run()

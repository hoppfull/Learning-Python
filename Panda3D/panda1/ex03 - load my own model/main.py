import direct.showbase.ShowBase as panda3d_SB

class MyApp(panda3d_SB.ShowBase):
    def __init__(self):
        panda3d_SB.ShowBase.__init__(self)

        # Make sure models are not stored in "models/" or panda3d will look inside the sdk
        self.icosphere = self.loader.loadModel("myModels/icosphere")
        self.icosphere.reparentTo(self.render)

if __name__ == "__main__":
    app = MyApp()
    app.run()

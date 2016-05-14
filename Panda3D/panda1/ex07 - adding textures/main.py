import direct.showbase.ShowBase as p3d_SB

class MyApp(p3d_SB.ShowBase):
    def __init__(self):
        p3d_SB.ShowBase.__init__(self)

        self.mymodel = self.loader.loadModel("res/models/mymodel")
        self.mymodel.reparentTo(self.render)
        self.mymodel.setTexture(self.loader.loadTexture("res/textures/mymodel_colormap.png"))

if __name__ == "__main__":
    app = MyApp()
    app.run()

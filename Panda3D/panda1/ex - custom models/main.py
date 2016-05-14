import direct.showbase.ShowBase as p3d_SB #Panda3D framework

class MyApp(p3d_SB.ShowBase):
    def __init__(self):
        p3d_SB.ShowBase.__init__(self)

        # Create a nodepath to hold our model
        self.mybox_model = loader.loadModel("mybox")
        # Parent the nodepath under render in the scenegraph
        self.mybox_model.reparentTo(self.render)

if __name__ == "__main__":
    app = MyApp()
    app.run()

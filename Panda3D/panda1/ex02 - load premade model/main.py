import direct.showbase.ShowBase as panda3d_SB

class MyApplication(panda3d_SB.ShowBase):
    def __init__(self):
        panda3d_SB.ShowBase.__init__(self)

        # Load model "environment.egg" from the SDK:
        self.environ = self.loader.loadModel("models/box")
        # Reparent the model to "render" in the scene graph:
        self.environ.reparentTo(self.render)

if __name__ == "__main__":
    application = MyApplication()
    application.run()

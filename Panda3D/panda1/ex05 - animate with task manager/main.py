import direct.showbase.ShowBase as p3D_SB
import direct.task as p3d_TSK

class MyApp(p3D_SB.ShowBase):
    def __init__(self):
        p3D_SB.ShowBase.__init__(self)

        self.environ = self.loader.loadModel("models/environment")
        self.environ.reparentTo(self.render)
        self.environ.setScale(0.1, 0.1, 0.1)

        self.icosphere = self.loader.loadModel("res/models/icosphere")
        self.icosphere.reparentTo(self.render)

        self.taskMgr.add(self.bounceBall, "bounce ball!")

    def bounceBall(self, taskname):
        if self.icosphere.getZ() != 0:
            self.icosphere.setPos(0,0,0)
        else:
            self.icosphere.setPos(0,0,3)
        return p3d_TSK.Task.cont

if __name__ == "__main__":
    app = MyApp()
    app.run()

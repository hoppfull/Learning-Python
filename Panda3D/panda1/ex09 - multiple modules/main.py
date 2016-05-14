import direct.showbase.ShowBase as p3d_SB
import extra

class MyApp(p3d_SB.ShowBase):
    def __init__(self):
        p3d_SB.ShowBase.__init__(self)

        ico = extra.IcoSphere()
        ico.getModel().reparentTo(self.render)
        

if __name__ == "__main__":
    app = MyApp()
    app.run()

import direct.showbase.ShowBase as Panda3D_SB

class MainApplication(Panda3D_SB.ShowBase):
    def __init__(self):
        Panda3D_SB.ShowBase.__init__(self)

if __name__ == "__main__":
    application = MainApplication()
    application.run()

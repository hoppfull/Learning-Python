import direct.showbase.ShowBase as p3d_SB
import direct.interval.IntervalGlobal as p3d_IG
import panda3d.core as p3d_Core

class MyApp(p3d_SB.ShowBase):
    def __init__(self):
        p3d_SB.ShowBase.__init__(self)

        self.icosphere = self.loader.loadModel("res/models/icosphere")
        self.icosphere.reparentTo(self.render)

        p3d_IG.Sequence( #Executes a series of intervals
            self.icosphere.posInterval(10, #Duration for interval in sec
                                       p3d_Core.Point3(0,0,5), #Final position
                                       startPos=p3d_Core.Point3(0,0,-5)) #Starting position
            ).start() #One time fire on intervals
"""
        p3d_IG.Sequence(
            self.icosphere.posInterval(1,
                                       p3d_Core.Point3(0,0,5),
                                       startPos=p3d_Core.Point3(0,0,-5)),
            self.icosphere.posInterval(1,
                                       p3d_Core.Point3(0,0,-5),
                                       startPos=p3d_Core.Point3(0,0,5))
            ).loop() #Infinite repeat fire on intervals
"""

if __name__ == "__main__":
    app = MyApp()
    app.run()

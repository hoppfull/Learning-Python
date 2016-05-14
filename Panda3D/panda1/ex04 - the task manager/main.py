import direct.showbase.ShowBase as panda3d_SB
import direct.task as panda3d_TSK

class MyApp(panda3d_SB.ShowBase):
    def __init__(self):
        panda3d_SB.ShowBase.__init__(self)

        """The next line tells Panda3D's task manager to call the function
        'myFunction' and give it a name which the task will pass to the function"""
        self.taskMgr.add(self.myFunction, "task name")

    def myFunction(self, PENIS):
        """'PENIS' is assigned a string, the task name when this function
        is called by the task manager"""
        print PENIS

        """if Task.cont > 0 then task manager will keep calling this function
        each frame. Not sure if it ever changes"""
        return panda3d_TSK.Task.cont

if __name__ == "__main__":
    app = MyApp()
    app.run()

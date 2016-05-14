import MyPad360

class Fighter():
    def __init__(self):
        self.fighter_np = loader.loadModel("res/models/fighter")
        self.fighter_np.setScale(0.1, 0.1, 0.1)
        self.mypad = MyPad360.MyPad360()
        self.mypad.setupMyPad360()
        
    def spawnFighter(self):
        self.fighter_np.reparentTo(render)
        
        self.fighter_target_np = render.attachNewNode("Fighter lookAt Target")
        self.fighter_target_np.reparentTo(self.fighter_np)
        self.fighter_target_np.setCompass()
        
        self.dx = 0
        self.dy = 0
        
    def controlFighter(self, task):
        for e in self.mypad.events():
            if e.type == self.mypad.AXISMOTION:
                self.delta(e.jaxis.axis, e.jaxis.value)
                
        self.fighter_np.setPos(self.fighter_np.getX() + self.dx, self.fighter_np.getY() + self.dy, 0.4)
        self.fighter_np.lookAt(self.fighter_target_np)
        self.fighter_np.setR(-2.0*self.fighter_np.getH())
        return task.again
        
    def delta(self, axis, thrust):
        
        if axis == 0 or axis == 1:
            thrust /= 5000.0
            thrust = 0.005*abs(thrust)*thrust
        
            if axis == 0:
                self.dx = thrust
            elif axis == 1:
                self.dy = -thrust
        
        elif (axis == 2)and(thrust < -2000 or thrust > 2000):
            self.fighter_target_np.setX(thrust)
        elif (axis == 3)and(thrust < -2000 or thrust > 2000):
            self.fighter_target_np.setY(-thrust)
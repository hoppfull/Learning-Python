import numpy as np

class ProjectionMatrix():
    """This matrix provides projection distortion.
    Projection distortion is when things that are far away
    appear smaller and things that are close appear bigger.
    This works flawlessly so far. Takes in screen-size and
    provides near- and far clipping. fov is field-of-view
    and smaller values will make view zoom in. A value of 1
    will provide a panorama image."""
    def __init__(self, screen_size, zNear, zFar, fov):
        if fov >= 1: # Limit to 0.99 or we get infinity error at 1.0. >1.0 will give strange result.
            fov = 0.99999;
            
        tanHalfFOV = np.tan(fov * np.pi / 2.0)
        zRange = zNear - zFar;
        
        self.projectionMatrix = np.array([
                [ # Row 0:
                    screen_size[1] / (tanHalfFOV * screen_size[0]),
                    0,
                    0,
                    0
                ],
                [ # Row 1:
                    0,
                    1.0 / tanHalfFOV,
                    0,
                    0
                ],
                [ # Row 2:
                    0,
                    0,
                    (-zNear - zFar)/zRange,
                    2.0 * zFar * zNear / zRange
                ],
                [ # Row 3:
                    0,
                    0,
                    1,
                    0
                ],
            ], dtype=np.float32)
            
    def get(self):
        return self.projectionMatrix
    
class ViewMatrix():
    """This matrix transform a model as if it's percieved by a
    camera with a target 'self.t' in global world coordinates
    and a position 'self.p' in global world coordinates. Global
    coordinates are x=right, y=forth and z=up."""
    def __init__(self, position):
        self.p = vec3(position.x, position.y, position.z)
        # target coordinates:
        self.t = vec3(0, 0, 0)
        # tolerance value:
        self.tolerance = 0.5
        """The tolerance value is for testing when view lies within bounds.
        In case of 'self.orbitTarget()', it's for testing when view gets too
        close to target z-axis. In case of 'self.approachTarget()', it's for
        testing when view gets too close to target coordinates."""
        # Sensitivity value:
        self.alpha = 0.01
        """The sensitivity value is for tuning how sensitive 'self.orbitTarget()'
        and 'self.approachTarget()' are to user input."""
        
        # Initialize the rotationMatrix as the identity matrix:
        self.rotationMatrix = np.matrix([
            [1, 0, 0, 0],
            [0, 1, 0, 0],
            [0, 0, 1, 0],
            [0, 0, 0, 1]
            ], dtype=np.float32)
    
    def translate(self, dp):
        self.p = self.p.add(dp)
    
    def setPos(self, p):
        self.p = vec3(p.x, p.y, p.z)
    
    def lookAt(self, target=None, up=None):
        """This function focuses the view on a target.
        Tested and seem to work as it should... ........finally........"""
        if target != None:
            self.t = vec3(target.x, target.y, target.z)
        f = self.t.sub(self.p).norm()
        
        if up != None:
            u = vec3(up.x, up.y, up.z).norm()
        else:
            u = vec3(0, 0, 1)
        
        s = f.cross(u).norm() # f x u
        u = s.cross(f) # s x f, automatically normalized
        
        self.rotationMatrix = np.matrix([
            [ s.x, s.y, s.z, 0],
            [ u.x, u.y, u.z, 0],
            [ f.x, f.y, f.z, 0],
            [   0,   0,   0, 1]], dtype=np.float32)
    
    def approachTarget(self, amount):
        """This function approaches the view towards the target
        when amount is positive and moves away from the target when
        amount is negative. It will stay outside the self.tolerance
        distance. When completely close to the target, view cannot
        look up or down too much."""
        if amount == 0:
            # If amount is zero, do nothing.
            return
        
        if self.t.sub(self.p).mag()*(1 - amount) > 2.0*self.tolerance:
            # If 'self.approachTarget()' will not take the view within twice the
            # tolerance distance, approach the target by given amount:
            self.p = self.p.add(self.t.sub(self.p).scale(amount))
        
        
    def orbitTarget(self, axis):
        if axis == (0, 0):
            return # Do nothing
        
        # Get target2camera-vector:
        p = self.p.sub(self.t)
        
        # Assign passed values to variables we can change if we have to:
        axis_x = -axis[0]
        if axis[1] > 0.30/self.alpha:
            """If axis[1] is bigger than 0.40 / self.alpha, we get strange results
            becouse view can 'tunnel' over the boundary set when getting view is
            getting close to target z-axis. Changing tolerance doen't change it a
            whole lot so I'm setting a boundary value for axis[1] to +-0.30 / self.alpha which is
            really really large as it is."""
            axis_y = 0.3 / self.alpha
        elif axis[1] < -0.30/self.alpha:
            axis_y = -0.3 / self.alpha
        else:
            axis_y = axis[1]
        
        
        if axis_y > 0 and p.z > 0:
            """Tests if user is trying to orbit the view up
            and if the view is above the 'equator'. The second
            test is to make sure the view doesn't get stuck
            if it gets inside the tolerance bounds and can get back
            out as long as it's trying to move away."""
            if vec2(p.x, p.y).mag() < self.tolerance:
                axis_y = 0
        elif axis_y < 0 and p.z < 0:
            """Tests if user is trying to orbit the view down
            and if the view is below the 'equator'. Same test 
            but for different case as the one above."""
            if vec2(p.x, p.y).mag() < self.tolerance:
                axis_y = 0
        
        if axis_y == 0: #If the other axis is zero:
            # Amount of rotation for target-cam x-axis: (longitude, west2east)
            v = vec3(0, 0, 1) # v is up vector
            rate = axis_x
            
        elif axis_x == 0: #If the other axis is zero:
            # Amount of rotation for target-cam y-axis: (latitude, south2north)
            v = p.cross(vec3(0, 0, 1)).norm() # v is side vector
            rate = axis_y
        
        else: #If neither is zero
            # u is up vector:
            u = vec3(0, 0, axis_x)
            # s is side vector:
            s = p.cross(vec3(0, 0, 1)).norm().scale(axis_y)
            
            # v is combined vector:
            v = u.add(s).norm()
            rate = abs(axis_x) + abs(axis_y)
        
        sin = np.sin(self.alpha * rate)
        cos = np.cos(self.alpha * rate)
        
        rotateMatrix = np.matrix([
                [ # Row 0:
                    ( v.x*v.x*(1 - cos) +     cos ),
                    ( v.y*v.x*(1 - cos) - v.z*sin ),
                    ( v.z*v.x*(1 - cos) + v.y*sin ),
                    0
                ],
                [ # Row 1:
                    ( v.x*v.y*(1 - cos) + v.z*sin ),
                    ( v.y*v.y*(1 - cos) +     cos ),
                    ( v.z*v.y*(1 - cos) - v.x*sin ),
                    0
                ],
                [ # Row 2:
                    ( v.x*v.z*(1 - cos) - v.y*sin ),
                    ( v.y*v.z*(1 - cos) + v.x*sin ),
                    ( v.z*v.z*(1 - cos) +     cos ),
                    0
                ],
                [ # Row 3:
                    0,
                    0,
                    0,
                    1
                ],
            ], dtype=np.float32)
            
        p = rotateMatrix.dot( np.array([p.x, p.y, p.z, 1.0]) ).getA()[0][0:3]
        self.p = vec3(p[0], p[1], p[2]).add(self.t)
        self.lookAt(self.t)
    
    def get(self):
        translationMatrix = np.matrix([
            [1,0,0,-self.p.x],
            [0,1,0,-self.p.y],
            [0,0,1,-self.p.z],
            [0,0,0,1]
            ], dtype=np.float32)
            
        return (self.rotationMatrix*translationMatrix).getA()
    
class ModelMatrix():
    """This matrix transform a model into world coordinates.
    Heavily tested and should work properly. Could probably
    be optimized further or even translated into cython for
    performance."""
    def __init__(self, position):
        self.p = vec3(position.x, position.y, position.z)
        self.s = vec3(1, 1, 1)
        
        self.rotationMatrix = np.matrix([
            [1, 0, 0, 0],
            [0, 1, 0, 0],
            [0, 0, 1, 0],
            [0, 0, 0, 1]
            ], dtype=np.float32)
    
    def translate(self, dp):
        self.p = self.p.add(dp)
    
    def rotate(self, turns, unit):
        """Heavily tested and should work! Requires 'GL_TRUE'
        to be passed to the uniform on shader program to work."""
        
        u = unit.norm()
        sin = np.sin(turns * np.pi * 2)
        cos = np.cos(turns * np.pi * 2)
        
        self.rotationMatrix = self.rotationMatrix.dot(
            np.matrix([
                [ # Row 0:
                    ( u.x*u.x*(1 - cos) +     cos ),
                    ( u.y*u.x*(1 - cos) - u.z*sin ),
                    ( u.z*u.x*(1 - cos) + u.y*sin ),
                    0
                ],
                [ # Row 1:
                    ( u.x*u.y*(1 - cos) + u.z*sin ),
                    ( u.y*u.y*(1 - cos) +     cos ),
                    ( u.z*u.y*(1 - cos) - u.x*sin ),
                    0
                ],
                [ # Row 2:
                    ( u.x*u.z*(1 - cos) - u.y*sin ),
                    ( u.y*u.z*(1 - cos) + u.x*sin ),
                    ( u.z*u.z*(1 - cos) +     cos ),
                    0
                ],
                [ # Row 3:
                    0,
                    0,
                    0,
                    1
                ],
            ], dtype=np.float32))
    
    def scale(self, s):
        self.s = vec3(s.x, s.y, s.z)
    
    def lookAt(self, target, up=None):
        """Heavily tested and should work! Requires 'GL_TRUE'
        to be passed to the uniform on shader program to work."""
        
        # Get normalized vector pointing from model to target
        f = target.sub(self.p).norm()
        if up != None:
            u = vec3(up.x, up.y, up.z).norm()
        else:
            u = vec3(0, 0, 1)
        
        s = f.cross(u).norm() # f x u
        # s must be normalized! Consider when f and u are not perpendicular!
        u = s.cross(f) # s x f, automatically normalized
        
        self.rotationMatrix = np.matrix([
            [ s.x, f.x, u.x, 0],
            [ s.y, f.y, u.y, 0],
            [ s.z, f.z, u.z, 0],
            [   0,   0,   0, 1]], dtype=np.float32)
    
    def get(self):
        """Heavily tested and should work! Requires 'GL_TRUE'
        to be passed to the uniform on shader program to work."""
        translationMatrix = np.matrix([
            [1,0,0,self.p.x],
            [0,1,0,self.p.y],
            [0,0,1,self.p.z],
            [0,0,0,1]
            ], dtype=np.float32)
        
        scaleMatrix = np.matrix([
            [self.s.x,0,0,0],
            [0,self.s.y,0,0],
            [0,0,self.s.z,0],
            [0,0,0,1]
            ], dtype=np.float32)
        
        return (translationMatrix*self.rotationMatrix*scaleMatrix).getA()
    
class quaternion():
    def __init__(self, x, y, z, w):
        self.x = float(x)
        self.y = float(y)
        self.z = float(z)
        self.w = float(w)
        
    def mag(self): # Get length of quaternion
        return np.sqrt(self.x*self.x + self.y*self.y + self.y*self.y + self.y*self.y)
        
    def norm(self): # Normalize quaternion
        return quaternion(
            x= self.x / self.mag(),
            y= self.y / self.mag(),
            z= self.z / self.mag(),
            w= self.w / self.mag())
            
    def conjugate(self):
        return quaternion(
            x=-self.x,
            y=-self.y,
            z=-self.z,
            w= self.w)
            
    def xQ(self, q): # Multiply with quaternion
        return quaternion(
            x= self.x * q.w + self.w * q.x + self.y * q.z - self.z * q.y,
            y= self.y * q.w + self.w * q.y + self.z * q.x - self.x * q.z,
            z= self.z * q.w + self.w * q.z + self.x * q.y - self.y * q.x,
            w= self.w * q.w - self.x * q.x - self.y * q.y - self.z * q.z)
    
    def xV(self, v): # Multiply with vector
        return quaternion(
            x= self.w*v.x + self.y*v.z - self.z*v.y,
            y= self.w*v.y + self.z*v.x - self.x*v.z,
            z= self.w*v.z + self.x*v.y - self.y*v.x,
            w=-self.x*v.x - self.y*v.y - self.z*v.z)

class vec2():
    def __init__(self, x, y):
        self.x = float(x)
        self.y = float(y)
        
    def mag(self):
        return np.sqrt(self.x*self.x + self.y*self.y)
    
    def norm(self):
        return vec2(
            x= self.x / self.mag(),
            y= self.y / self.mag())
    
    
class vec3():
    def __init__(self, x, y, z):
        self.x = float(x)
        self.y = float(y)
        self.z = float(z)
        
    def cross(self, vector):
        return vec3(
            x= self.y*vector.z - self.z*vector.y,
            y= self.z*vector.x - self.x*vector.z,
            z= self.x*vector.y - self.y*vector.x)
        
    def dot(self, vector):
        return float( self.x*vector.x + self.y*vector.y + self.z*vector.z )
    
    def mag(self):
        return np.sqrt(self.x*self.x + self.y*self.y + self.z*self.z)
    
    def norm(self):
        return vec3(
            x= self.x / self.mag(),
            y= self.y / self.mag(),
            z= self.z / self.mag())
            
    def add(self, vector):
        return vec3(
            x= self.x + vector.x,
            y= self.y + vector.y,
            z= self.z + vector.z)
            
    def sub(self, vector):
        return vec3(
            x= self.x - vector.x,
            y= self.y - vector.y,
            z= self.z - vector.z)
            
    def scale(self, scalar):
        return vec3(
            self.x*scalar,
            self.y*scalar,
            self.z*scalar)
        
    def rotate(self, angle, axis):
        pass

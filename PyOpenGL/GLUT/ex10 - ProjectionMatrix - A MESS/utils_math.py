import numpy as np

class ProjectionMatrix(): ##TODO: Test this to see if it works properly
    def __init__(self, width, height, zNear, zFar, fov):
        if fov >= 1: # Limit to 0.99 or we get infinity error at 1.0. >1.0 will give strange result.
            fov = 0.999;
        
        tanHalfFOV = np.tan(fov * np.pi / 2.0)
        zRange = zNear - zFar;
        
        self.projectionMatrix = np.array([
                [ # Row 0:
                    height / (tanHalfFOV * width),
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
        
class ViewMatrix(): # CameraMatrix
    def __init__(self,
        position=np.array([0, 0, 0], dtype=np.float32)):
        self.position = position
        self.setDirection()
            
    def rotate(self, turns, unit): # Right hand rule of rotation!
        sin = np.sin(-turns * 6.283185307179586)
        cos = np.cos(-turns * 6.283185307179586)
        a, b, c = unit[0], unit[1], unit[2]
        
        self.rotationMatrix = self.rotationMatrix.dot(
            np.matrix([
                [ # Row 0:
                    ( a*a*(1 - cos) +   cos ),
                    ( b*a*(1 - cos) - c*sin ),
                    ( c*a*(1 - cos) + b*sin ),
                    0
                ],
                [ # Row 1:
                    ( a*b*(1 - cos) + c*sin ),
                    ( b*b*(1 - cos) +   cos ),
                    ( c*b*(1 - cos) - a*sin ),
                    0
                ],
                [ # Row 2:
                    ( a*c*(1 - cos) - b*sin ),
                    ( b*c*(1 - cos) + a*sin ),
                    ( c*c*(1 - cos) +   cos ),
                    0
                ],
                [ # Row 3:
                    0,
                    0,
                    0,
                    1
                ],
            ], dtype=np.float32))
    
    def translate(self, dpos):
        self.position += dpos
    
    def setPosition(self, pos):
        self.position = np.array(pos, dtype=np.float32)
    
    def setDirection(self, forward=(0, 1, 0), up=(0, 0, 1)):
        # http://www.cs.virginia.edu/~gfx/Courses/1999/intro.fall99.html/lookat.html
        f = np.array(forward, dtype=np.float32)
        u = np.array(up, dtype=np.float32)
        
        if np.linalg.norm(f) == 0: # If bad forward vector was passed, set default
            f = np.array([0,1, 0], dtype=np.float32)
        else: # If good vector was passed, normalize f to unitvector
            f /= np.linalg.norm(f)
        
        if np.linalg.norm(u) == 0: # If bad up vector was passed, set default
            u = np.array([0, 0, 1], dtype=np.float32) # No point in normalizing u
        
        s = np.cross(f, u) # f x u
        s /= np.linalg.norm(s) # No matter the length of u, s has to be normalized
        u = np.cross(s, f) # Since both f and s are normalized and perpendicular, so is automatically u normalized
        
        self.rotationMatrix = np.matrix([
                [ # Row 0:
                    s[0],
                    s[1],
                    s[2],
                    0
                ],
                [ # Row 1:
                    u[0],
                    u[1],
                    u[2],
                    0
                ],
                [ # Row 2:
                    f[0],
                    f[1],
                    f[2],
                    0
                ],
                [ # Row 3:
                    0,
                    0,
                    0,
                    1
                ]
            ], dtype=np.float32)
        
    def get(self):
        translationMatrix = np.matrix([
            [1,0,0,-self.position[0]],
            [0,1,0,-self.position[1]],
            [0,0,1,-self.position[2]],
            [0,0,0,1]
            ], dtype=np.float32)
        
        return self.rotationMatrix.dot(translationMatrix).getA()

class ModelMatrix(): # TranslationRotationScaleMatrix
    def __init__(self,
        position=np.array([0, 0, 0], dtype=np.float32),
        scale=np.array([1, 1, 1], dtype=np.float32)):
        
        self.position = position
        self.scale = scale
        
        self.rotationMatrix = np.matrix([
            [1, 0, 0, 0],
            [0, 1, 0, 0],
            [0, 0, 1, 0],
            [0, 0, 0, 1]
            ], dtype=np.float32)
    
    def translate(self, dpos):
        self.position += dpos
    
    def rotate(self, turns, unit): # Right hand rule of rotation!
        sin = np.sin(turns * 6.283185307179586)
        cos = np.cos(turns * 6.283185307179586)
        a, b, c = unit[0], unit[1], unit[2]
        
        self.rotationMatrix = self.rotationMatrix.dot(
            np.matrix([
                [ # Row 0:
                    ( a*a*(1 - cos) +   cos ),
                    ( b*a*(1 - cos) - c*sin ),
                    ( c*a*(1 - cos) + b*sin ),
                    0
                ],
                [ # Row 1:
                    ( a*b*(1 - cos) + c*sin ),
                    ( b*b*(1 - cos) +   cos ),
                    ( c*b*(1 - cos) - a*sin ),
                    0
                ],
                [ # Row 2:
                    ( a*c*(1 - cos) - b*sin ),
                    ( b*c*(1 - cos) + a*sin ),
                    ( c*c*(1 - cos) +   cos ),
                    0
                ],
                [ # Row 3:
                    0,
                    0,
                    0,
                    1
                ],
            ], dtype=np.float32))
    
    def setPosition(self, pos):
        self.position = np.array(pos, dtype=np.float32)
    
    def setDirection(self, forward=(0, 1, 0), up=(0, 0, 1)):
        # http://www.cs.virginia.edu/~gfx/Courses/1999/intro.fall99.html/lookat.html
        f = np.array(forward, dtype=np.float32)
        u = np.array(up, dtype=np.float32)
        
        if np.linalg.norm(f) == 0: # If bad forward vector was passed, set default
            f = np.array([0,1, 0], dtype=np.float32)
        else: # If good vector was passed, normalize f to unitvector
            f /= np.linalg.norm(f)
        
        if np.linalg.norm(u) == 0: # If bad up vector was passed, set default
            u = np.array([0, 0, 1], dtype=np.float32) # No point in normalizing u
        
        s = np.cross(f, u) # f x u
        s /= np.linalg.norm(s) # No matter the length of u, s has to be normalized
        u = np.cross(s, f) # Since both f and s are normalized and perpendicular, so is automatically u normalized
        
        self.rotationMatrix = np.matrix([
                [ # Row 0:
                    -s[0],
                    -s[1],
                    -s[2],
                    0
                ],
                [ # Row 1:
                    f[0],
                    f[1],
                    f[2],
                    0
                ],
                [ # Row 2:
                    u[0],
                    u[1],
                    u[2],
                    0
                ],
                [ # Row 3:
                    0,
                    0,
                    0,
                    1
                ]
            ], dtype=np.float32)
    
    def setScale(self, scale):
        self.scale = np.array(scale, dtype=np.float32)
    
    def get(self): # Create and combine translation-, rotation- and scale-matrix
        translationMatrix = np.matrix([
            [1,0,0,self.position[0]],
            [0,1,0,self.position[1]],
            [0,0,1,self.position[2]],
            [0,0,0,1]
            ], dtype=np.float32)
        
        scaleMatrix = np.matrix([
            [self.scale[0],0,0,0],
            [0,self.scale[1],0,0],
            [0,0,self.scale[2],0],
            [0,0,0,1]
            ], dtype=np.float32)
        # The order in which they affect a vector is read from right to left: (Order matters!)
        return translationMatrix.dot(self.rotationMatrix.dot(scaleMatrix)).getA()
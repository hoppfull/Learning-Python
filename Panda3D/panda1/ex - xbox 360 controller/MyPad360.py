import sys
import sdl2
import sdl2.ext

##Ignoring rumbling for now until I can figure out how that works

class MyPad360():
    def __init__(self):
        if sdl2.SDL_Init(sdl2.SDL_INIT_JOYSTICK | sdl2.SDL_INIT_HAPTIC):
            raise RuntimeError(sdl2.SDL_GetError())
        
        self.BUTTONDOWN = sdl2.SDL_JOYBUTTONDOWN
        self.BUTTONUP = sdl2.SDL_JOYBUTTONUP
        self.AXISMOTION = sdl2.SDL_JOYAXISMOTION
        self.HATMOTION = sdl2.SDL_JOYHATMOTION
        
        if sys.platform == "win32" or sys.platform == "cygwin": # Mappings for Windows:
            self.BUTTON_ID = ["DPAD_UP", "DPAD_DOWN", "DPAD_LEFT", "DPAD_RIGHT", "START", "BACK", "LSTICK", "RSTICK", "LB", "RB", "A", "B", "X", "Y", "XBOX"]
            self.AXIS_ID = ["LSTICK_H", "LSTICK_V", "RSTICK_H", "RSTICK_V", "LT", "RT"]
        else: # Default mappings for Linux:
            self.BUTTON_ID = ["A", "B", "X", "Y", "LB", "RB", "BACK", "START", "XBOX", "LSTICK", "RSTICK", "DPAD_LEFT", "DPAD_RIGHT", "DPAD_UP", "DPAD_DOWN"]
            self.AXIS_ID = ["LSTICK_H", "LSTICK_V", "RSTICK_H", "RSTICK_V", "RT", "LT"]
        
    def setupMyPad360(self):
        count = sdl2.joystick.SDL_NumJoysticks()
        
        for i in range(count):
            joystick = sdl2.SDL_JoystickOpen(i)
        
        # Make sure init-events are ignored:
        for e in sdl2.ext.get_events():
            pass
    
    def getNumControllers(self):
        return sdl2.joystick.SDL_NumJoysticks()
    
    def events(self):
        # Return all unhandled events and deal with them in main program
        return sdl2.ext.get_events()
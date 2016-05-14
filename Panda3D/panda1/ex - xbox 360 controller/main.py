import MyPad360

mypad = MyPad360.MyPad360()
mypad.setupGamepads()

# This while-loop could be a task that repeats with a given frequency:
while True:
    for e in mypad.events():
        # XBox360 Controller-BUTTONS:
        # "e.type == mypad.BUTTONDOWN" tests if current event is a button press
        # "e.type == mypad.BUTTONUP" tests if current event is a button release
        # "e.jbutton.button" number ID for which button produced current event
        # "e.jbutton.which" tells you which controller is producing current button event
        
        # XBox360 Controller-STICKS and -TRIGGERS:
        # "e.type == mypad.AXISMOTION" tests if current event is a change with the sticks (VERY sensitive!)
        # "e.jaxis.axis" gives number ID for which stick caused current event and in which direction:
            # 0: left stick in left and right position
            # 1: left stick in back and forth position
            # 2: right stick in left and right position
            # 3: right stick in back and forth position
            # 4: left trigger
            # 5: right trigger
        # "e.jaxis.value" gives a value of position for which stick caused current event
            # Value ranges from -32767 to +32767 (left to right or forth to back for sticks), (released to pressed for triggers)
        # "e.jhat.which" tells you which controller is producing current stick event
        
        
        # Example code:
        if e.type == mypad.BUTTONDOWN:
            print "Pressed: ", mypad.BUTTON_ID[e.jbutton.button], "on controller!"
            
        elif e.type == mypad.BUTTONUP:
            print "Released: ", mypad.BUTTON_ID[e.jbutton.button], "on controller!"
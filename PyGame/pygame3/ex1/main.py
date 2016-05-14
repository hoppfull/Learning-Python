import pygame as pg
import myGameEngine as myGE

class main(myGE.GameEngine):
	def __init__(self):
		myGE.GameEngine.__init__(self)
	
myGameObject = main()
myGameObject.mainLoop()
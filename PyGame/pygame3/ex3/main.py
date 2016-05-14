import pygame as pg
import myGameEngine as myGE
import sys #Imported for argv and loading settings.txt

with open(sys.argv[1], 'r') as txt: ##LOADING SETTINGS FROM EXTERNAL FILE!
	exec(txt.read()) #Settings from external file are initialized in variable 'settings'
del txt #Cleanup

class main(myGE.GameEngine):
	def __init__(self):
		self.s = settings
		myGE.GameEngine.__init__(self, self.s['$res'], self.s['$fps'])
		self.icon = self.s['$icon'] #this line can be removed if needed
		self.caption = self.s['$name'] #this line can be removed if needed
		
	def mouseUp(self, button, pos):
		if(button == 1):
			print("left click!")
		if(button == 2):
			print("middle click!")
		if(button == 3):
			print("right click!")

	def draw(self):
		self.screen.fill(self.s["$bg_col"])

myGameObject = main()
myGameObject.mainLoop()
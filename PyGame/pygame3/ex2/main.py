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
		pg.display.set_caption(self.s['$name'])
		
	def console(self): #Any information I want to be shown in the python console should be defined in this function
		pass
		
	def draw(self):
		self.screen.fill(self.s["$bg_col"])

myGameObject = main()
myGameObject.mainLoop()
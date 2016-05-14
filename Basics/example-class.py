class song(object): ##object verkar vara krav och är inte ett godtyckligt namn
	def __init__(self): ##self är ett godtyckligt namn. Standard antar jag. Men den måste vara med verkar det som.
		# self.lyrics = "hello singalong!"
		# self.kuk = "sing song ching chong!"
		# self.snopp = my_argument
		pass
	
	def sing(self):
		# print(self.lyrics)
		# print(self.kuk * 2)
		# print(self.snopp)
		print("Hello class!")
	
mySong = song() ##en instance av min class song skapas

mySong.sing() ##instansen mySong kör funktionen sing
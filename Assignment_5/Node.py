#Node designed to be a block in my maze
class Node(object):
	#Thinking location will be an x and y coordinate
	def __init__ (self,value):
		self.x= int(0)
		self.y= int(0)
		self.parent= None
		#don't know value yet but should initialize
		self.util= float(0)
		self.reward= int(0)
		self.value=value

	#Can make functionality within class

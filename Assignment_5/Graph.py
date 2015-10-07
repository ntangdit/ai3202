import Node

class Graph(object):
	def __init__(self):
		data= []
	
	def addNode(self, Node):
		data.append(Node)
	
	def initCost(self):
		if data is None:
			return
		else:
			for block in self.data:
				#mountain
				if block.value is 1:
					block.reward= -1.0
				elif block.value is 3: #snake
					block.reward= -2.0
				elif block.value is 4: #barn
					block.reward= 1.0
				elif block.value is 50: #goal
					block.reward= 50.0
				#no need to assign the 0s or even the wall

	def findNode(self, x, y):
		if x<0 or y < 0:
			return None
		try:
			return self.data[x][y]
		except IndexError:
			return None
	
	#only giving a list of adjacent nodes
	def adj(self, node):
		adjacent= []
		up = findNode(self, x, y+1)
		down=findNode(self, x, y-1)
		left=findNode(self, x-1, y)
		right= findNode(self, x+1, y)
		for k in [up, down, left, right]:
			if k.value is 2:
				k = None
			else:
				adjacent.append(k)
			k.parent=node
		return adjacent		

			
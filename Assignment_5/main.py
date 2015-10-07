import Node
import readWorld
import Markov_Decision_Process
import Graph 


#Will take user input through argv. Need to read txt, call the MDP, 
#Will need to adjust MDP to iterate multiple times... 
#The hard part will be making a loop that will decide the best path. Should 
#print the values and location of best 
#def main(argv):

class Graph(object):
	def __init__(self):
		self.data= []
	
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

def readWorld(world, grp):
	for lines in world.readline():
		col= 0
		for char in lines:
			#Node not created yet, so I need to create the node here
			#Where is my value? should be char. Do I know where I am? col
			#What should I name the instance of the node?
			mahNo= Node(mahNo, char)
			mahNo.x= col
			mahNo.y= lines
			col = col +1
			grp.addNode(mahNo)
			
		
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

def mdp(graph, err):
	gama= 0.9
	delta = 0
	for block in graph.data:
		if block.value is not 0:
			continue
		else:			
			#adjacent= graph.adj(graph, end)
			#utility of all the options
			options= []
			adjacent = block.adj(graph, block)
			#This for loop only solves straying issue
			for state in adjacent:
				#Need to be able to go left/right of my action
				if state.x is block.x:
					sides= graph.findNode(graph,state.x -1,state.y).util
					sides+= graph.findNode(graph,state.x +1, state.y).util
					sides *=.1
				elif state.y is block.y:
					sides= graph.findNode(graph,state.x,state.y-1).util
					sides += graph.findNode(graph,state.x, state.y -1).util
					sides *= .1
				sides += state.util*.8
				options.append(sides)
			utp= block.reward+ (gama* max(options))
			if abs(block.util - utp) < err*(1-gama)/gama:
				delta= abs(block.util-utp)
			if utp > block.util:
				block.util= utp
			if delta < err* (1-gama)/gama:
				return
		
filename= 'World1MDP.txt'
txt = open(filename)
print txt.read()
world = Graph()
readWorld(txt,world)
print world.findNode(1,1)
mdp(world, .5)

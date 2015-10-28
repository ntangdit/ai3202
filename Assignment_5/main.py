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
		self.data.append(Node)
	
	def initCost(self):
		if self.data is None:
			return
		else:
			for block in self.data:
				#mountain
				if block.value is '1':
					block.reward= -1.0
					block.util= -1.0
				elif block.value is '3': #snake
					block.reward= -2.0
					block.util=-2.0
				elif block.value is '4': #barn
					block.reward= 1.0
					block.util= 1.0
				elif block is self.findNode(9,7): #goal
					block.reward= 50.0
					block.util= 50.0
				#no need to assign the 0s or even the wall

	def findNode(self, x, y):
		if x<0 or y < 0:
			return None
		else:
			for node in self.data:
				if node.x is x and node.y is y:
					return node
	
	
	#only giving a list of adjacent nodes
	def adj(self, node):
		adjacent= []
		up = self.findNode(node.x, node.y+1)
		down=self.findNode(node.x, node.y-1)
		left=self.findNode(node.x-1, node.y)
		right= self.findNode(node.x+1, node.y)
		for k in [up, down, left, right]:
			if k is not None:
				if k.value is '2':
					k.reward = None
					k.util= None
				else:
					adjacent.append(k)
				k.parent=node
			else: 
				continue
		return adjacent		

def readWorld(world, grp):
	yval= 7
	#Because I start from the top
	for lines in world:
		col= 0
		lines= lines.split()
		for char in lines:
			#char holds the value
			mahNo= Node(char)
			mahNo.x= col
			mahNo.y= yval
			col = col +1
			grp.addNode(mahNo)
		yval= yval -1
	return grp
			
		
class Node(object):
	#Thinking location will be an x and y coordinate
	def __init__ (self,value):
		self.x= int(0)
		self.y= int(0)
		self.parent= None
		#don't know value yet but should initialize
		self.util= float(0)
		self.reward= float(0)
		self.value=value

def mdp(graph, err):
	print "starting mdp"
	gama= 0.9
	delta = 1
	print err*(1-gama)/gama
	while delta > err*(1-gama)/gama:
		delta = 0
		for block in graph.data:
			if block.value is not '0':
				continue
			else:			
				#adjacent= graph.adj(graph, end)
				#utility of all the options
				options= []
				adjacent = graph.adj(block)
				#This for loop only solves straying issue
				
				
				for state in adjacent:
					#Need to be able to go left/right of my action
			#		print "adjacent is", state.x,state.y
					sides= float(0.0)
					
					if state.x is block.x:
						if graph.findNode(state.x-1, state.y) is not None:
							if graph.findNode(state.x-1, state.y).util is not None:
								sides= graph.findNode(state.x -1,state.y).util
						elif graph.findNode(state.x+1, state.y) is not None:
							if graph.findNode(state.x+1, state.y).util is not None:
								sides+= graph.findNode(state.x +1, state.y).util
						sides *= 0.1	
						
					elif state.y is block.y:
						if graph.findNode(state.x, state.y-1) is not None:
							if graph.findNode(state.x, state.y-1).util is not None:
								sides= graph.findNode(state.x,state.y-1).util
						elif graph.findNode(state.x, state.y-1) is not None:
							if graph.findNode(state.x, state.y-1).util is not None:
								sides = sides + graph.findNode(state.x, state.y -1).util
						sides *= .1
					sides = sides+ state.util*.8
					
					options.append(sides)
					#Will give me the optimal path by following the parents
					if sides is max(options):
						block.parent= state
					
				utp= block.reward+ (gama* max(options))
				if abs(block.util - utp) > delta:
					delta= abs(block.util-utp)
				block.util = utp


		
filename= 'World1MDP.txt'
#txt = open(filename)
#print txt.read()
with open(filename) as txt:
	world = Graph()
	world = readWorld(txt,world)
world.initCost()
print len(world.data)
print world.findNode(9,7).value
print "Node 9,7 has utility of ", world.findNode(9,7).reward
print world.findNode(1,3).util
print "A snake has a util of ", world.findNode(1,2).util
print "Adjacent utilities are " ,world.findNode(1,4).util,world.findNode(1,2).util,world.findNode(0,3).util
mdp(world, 0.5)
print world.findNode(6,4).value
print "Node 6,4 has utility of ", world.findNode(6,4).util
cursor = world.findNode(0,0)
while cursor is not world.findNode(9,7):
	print "I'm currently at ", cursor.x, " ", cursor.y
	print "Have utility of ", cursor.util
	cursor= cursor.parent
print "I made it to the goal of 50!"

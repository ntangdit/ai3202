import Node
import Graph
import readWorld

#end node will be made in the main. So will gama
#I'm going to iteratively go through all the states and assign values
#algorithm will be faster if I start from the 50 pts
def mdp(graph, end, err)
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
			if abs(end.util-utp)< err*(1-gama)/gama:
				delta= abs(block.util-utp))
			if utp > block.util:
				block.util= utp
			if delta < err* (1-gama)/gama:
				return
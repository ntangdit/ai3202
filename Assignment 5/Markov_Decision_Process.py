import Node
import Graph
import readWorld

#end node will be made in the main. So will gama
def mdp(graph, end, gama, err)
	#algorithm will be faster if I start from the 50 pts
	adjacent= graph.adj(graph, end)
	#utility of all the options
	options= []
	for state in adjacent:
		#Need to be able to go left/right of my action
		if state.x is end.x:
			sides= graph.findNode(graph,state.x -1,state.y).util
			sides+= graph.findNode(graph,state.x +1, state.y).util
			sides *=.1
		elif state.y is end.y:
			sides= graph.findNode(graph,state.x,state.y-1).util
			sides += graph.findNode(graph,state.x, state.y -1).util
			sides *= .1
		sides += state.util*.8
		#When I pick the value that is max, how do I know where it came from?
		options.append(sides)
	utp= end.util+ gama* max(options)
	if abs(end.util-utp)< err*(1-gama)/gama:
		return
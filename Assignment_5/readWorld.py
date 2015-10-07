import Node

#want to read the world file and put it into the graph
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
			

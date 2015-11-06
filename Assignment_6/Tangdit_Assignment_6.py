#Made by Nikolai Tangdit
#Collaborated with Prad Kikkeri

import getopt, sys

class Node(object):
	def __init__(self, name):
		self.name= name
		self.prior= 0.0
		self.probDist= None
		self.parent = None
		self.edge= []

class Graph(object):

	def __init__(self):
		self.data = []

	def worldinit(self):
		P = Node('P')
		P.prior = 0.9
		S = Node('S')
		S.prior = 0.3
		C= Node('C')
		C.parent = [P, S]
		P.edge = [C]
		S.edge = [C]
		C.probDist= {"low": {"T": 0.03, "F": 0.001}, "high": {"T":0.05, "F": 0.02}}
		X = Node('X')
		X.parent= [C]
		X.probDist= {"T": 0.9, "F": 0.2}
		D= Node('D')
		D.parent= [C]
		C.edge= [X,D]
		D.probDist= {"T": 0.65, "F": 0.30}
		self.data= [P,S,C,X,D]

	#will find the marginal of node
	def marginal(self, node):
		if node.name is 'P':
			return node.prior
		elif node.name is 'S':
			return 1- node.prior
		elif node.name is 'C':
			marg= (node.parent[1].prior)*node.probDist["high"]["T"]+(1-node.parent[1].prior)*node.probDist["high"]["F"]
			#P(s)*P(c|~p,s) + P(~s)*P(c|~p, ~s)
			marg *= (1-node.parent[0].prior)
			#Becomes P(~p)P(s)P(c|~p,s) + P(~p)P(~s)P(c|~p,~s)
			marg += (node.parent[0].prior)*((node.parent[1].prior)*node.probDist["low"]["T"]+(1-node.parent[1].prior)*node.probDist["low"]["F"])
			#P(~p)P(s)P(c|~p,s) + P(~p)P(~s)P(c|~p,~s) + P(p)P(s)P(c|p,s) + P(p)P(~s)P(c|p,~s)
			return marg
		elif node.name is 'X' or 'D':
			cancer_marg1=  node.parent[0].parent[1].prior * node.parent[0].probDist["high"]["T"]+ (1- node.parent[0].parent[1].prior)*node.parent[0].probDist["high"]["F"]
			cancer_marg1 *= (1- node.parent[0].parent[0].prior)
			cancer_marg2 = node.parent[0].parent[1].prior * node.parent[0].probDist["low"]["T"]+ (1- node.parent[0].parent[1].prior)*node.parent[0].probDist["low"]["F"]
			cancer_marg2 *= node.parent[0].parent[0].prior
			cancer_marg = cancer_marg1 + cancer_marg2
			#Now have cancer's marginal
			marg= cancer_marg* node.probDist["T"] + (1- cancer_marg)* node.probDist["F"]
			return marg

	def findNode(self, name):
		for node in self.data:
			if node.name is name:
				return node
		#failed to find the name
		print "Couldn't find node with that name"
	
	def condition(effect, cause):
		if cause in effect.parent:
			cause.probDist

	#input should be the node which should have same name as its char name
	def adjPrior(rv, newValue):
		if rv.name is not 'P' or 'S':
			return
		else:
			rv.prior= newValue
	
# Parser based on Prof. Hoenigman's	
	def getoptParser(self,opts, args):

		for o, a in opts:
			if o in ("-p"):
				print "flag", o
				print "args", a
				print a[0]
				print (a[1:])
				#setting the prior here works if the Bayes net is already built
				print self.adjPrior(self.findNode(a[0]), (a[1:]))
			elif o in ("-m"):
				print "flag", o
				print "args", a
				print (type(a))
				print self.marginal(self.findNode(a))
			elif o in ("-g"):
				print "flag", o
				print "args", a
				print type(a)
				'''you may want to parse a here and pass the left of |
				and right of | as arguments to calcConditional
				'''
				p = a.find("|")
				print a[:p]
				print a[p+1:]
				#calcConditional(a[:p], a[p+1:])
			elif o in ("-j"):
				print "flag", o
				print "args", a
			else:
				assert False, "unhandled option"




def main():
	bayes = Graph()
	bayes.worldinit()
	try:
		opts, args = getopt.getopt(sys.argv[1:], 'g:j:m:p:')
	except getopt.GetoptError as err:
		print(err)
		sys.exit(2)
	bayes.getoptParser(opts, args)
	
	
if __name__ == "__main__":
	main()
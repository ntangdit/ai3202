#Assignment 8 by Nikolai Tangdit
#Collaborated with Prad Kikkeri
import sys
import math
import copy

class Node(object):
	def __init__(self, letter, k):
		self.parent= None
		self.letter= letter
		self.time= k
		


class HMM(object):
	def __init__(self, data):
		#The array of tuples is data
		self.data= data
		self.letterEm= {}
		self.letterTr= {}
		self.letterInit= {}
		self.parent= None
		self.vertibiGraph= []
		#Create a table for each letter
		#Tables will be emission, transition, and initial probability
		for k in range(97, 123):
			#Inner key is X (state) outer key is E (Evidence)
			self.letterEm[chr(k)]= {}
			#Inner key is Xt outer key is Xt+1
			self.letterTr[chr(k)]= {}
			self.letterInit[chr(k)]= {0.038}
			#0.038 comes from 1/26, since I don't have a marginal value
			
	def probs(self, letter):
		s= 0.0
		OgvS= {}
		nexter= {}
		
		for m in range(0, len(self.data)-1):
			if self.data[m][0] is letter:
				s +=1
				#Protect from indexing outside of array
				try:
					if self.data[m+1][0] in nexter.keys():
						nexter[self.data[m+1][0]] += 1
					else:
						nexter[self.data[m+1][0]] = 1
				except IndexError:
					pass
				if self.data[m][1] in OgvS.keys():
					OgvS[self.data[m][1]] += 1
				else:
					OgvS[self.data[m][1]] = 1
		
		for state1 in self.letterEm.keys():
				if not self.letterEm[letter].has_key(state1):
					self.letterEm[letter][state1] = round(1.0/(s+27), 3)
		for state2 in self.letterEm.keys():
				if not self.letterTr[letter].has_key(state2):
					self.letterTr[letter][state2] = round(1.0/(s+27), 3)
		
		for key, val in nexter.items():
			self.letterTr[letter][key]= round((val+1)/(s+26), 3)
		for key, val in OgvS.items():
			self.letterEm[letter][key]= round((val+1)/(s+8),3)
		
		self.letterInit[letter]= round(s/len(self.data),3)

	def viterbi(self):
		#Will use array w/ dict inside to hold viterbi values
		#Might not need Whole_vit because I'm using nodes now
		Whole_vit= []
		#The key of tempV is a letter. The value is the probability weight.
		tempV= {}
		#Initial part of viterbi algorithm
		#I want to use letterEm[X:][E1]
		for initX in self.letterEm.keys():
			try:
				tempV[initX]= math.log(self.letterEm[initX][self.data[0][1]])+ math.log(self.letterInit[initX])
			except ValueError:
				pass
			intro= Node(initX,0)
			self.addNode(intro)
		Whole_vit.append(copy.deepcopy(tempV))
		tempV.clear()
		#Initializing outside of for loop to save memory (hopefully)
		bfrMax = {}
		#Will need to assign parents somewhere. Too tired to do it now
		for k in range(1, len(self.data)):
			#k is my time
			#Will use Whole_vit in order to optimize code
			for Xnow in self.letterEm.keys():
				for Xprev in Whole_vit[k-1].keys():
					#I have an array that holds all possibilities of Xt
					#P(Et|Xt)P(Xt|Xt-1)Vt-1[Xt-1]
					#Because Whole_vit will always be negative because dealing with really small numbers
					past = Whole_vit[k-1][Xprev] *-1
					try:
						bfrMax[Xprev]=(math.log(self.letterEm[Xnow][self.data[k][1]]) + math.log(self.letterTr[Xprev][Xnow]) + math.log(past))
					except ValueError:
						print self.letterEm[Xnow][self.data[k][1]],' ',self.letterTr[Xprev][Xnow],' ',Whole_vit[k-1][Xprev]
				print bfrMax
				maxKey= max(bfrMax, key=bfrMax.get)
				print "Did I ever make it here?"
				tempV[Xnow]=max(bfrMax[maxKey])
				#Will also use the max to assign parent to node... This is because I will 
				#be following it back from the terminal state. Each terminal state has a 
				#different path to it.
				#remove keys with values too small to be used
				for key, val in tempV.items():
					if val is 0.000:
						tempV.pop(key,None)
				point = Node(Xnow,k)
				point.parent= self.findNode(maxKey, k-1)
				self.addNode(point)
				bfrMax.clear()		
			#Add the dictionary I just made to Whole_viterbi
			Whole_vit.append(copy.deepcopy(tempV))
			tempV.clear()
		
		self.vertibiGraph= Whole_vit
		
	def addNode(self, Node):
		self.vertibiGraph.append(Node)
		
	def findNode(self, value, time):
		#assuming given correct parameters
		for node in self.vertibiGraph:
			if node.time is time and node.letter is value:
				return node
		
	def printer(self):
		print "For Emission Probabilities:\n\n"
		results = []
		for k in self.letterEm.keys():
			for ns, value in self.letterEm[k].items():
				strn = "P("+ns+"|"+k+") = " + str(value)
				results.append(strn)
		for m in sorted(results):
			print m
		print "\n\n For Transition Probabilities:\n\n"
		results = []
		for k in self.letterTr.keys():
			for ns, value in self.letterTr[k].items():
				strn = "P("+ns+"|"+k+") = " + str(value)
				results.append(strn)
		for m in sorted(results):
			print m
		
		print "\n\nMarginal Values: \n\n"
		for k in self.letterInit.keys():
			print "initial marginal for", k+":", self.letterInit[k]
			
			
	def printV(self, end):
		if end.parent is None:
			return
		print end.letter
		self.printV(end.parent)
 





if __name__ == '__main__':
	filename= 'typos20Test.data'
	typos= open(filename, 'r')
	dataR= []
	#Put all information into an array with tuples
	file= typos.readlines()
	for line in file:
		if line[0] is not '_':
			dataR.append((line[0], line[2]))
	markov= HMM(dataR)
	for letter in markov.letterEm.keys():
		markov.probs(letter)
	markov.viterbi()
	#markov.printV(markov.findNode(
	sys.stdout = open('output.txt', 'w')
	markov.printer()
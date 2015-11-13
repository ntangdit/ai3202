#Assignment 8 by Nikolai Tangdit
#Collaborated with Prad Kikkeri
import sys
import math

class HMM(object):
	def __init__(self, data):
		#The array of tuples is data
		self.data= data
		self.letterEm= {}
		self.letterTr= {}
		self.letterInit= {}
		#Create a table for each letter
		#Tables will be emission, transition, and initial probability
		for k in range(97, 123):
			self.letterEm[chr(k)]= {}
			self.letterTr[chr(k)]= {}
			self.letterInit[chr(k)]= {0.038}
			#0.038 comes from 1/26, since I don't have a marginal value
			
	def emission(self, output, given):
		s= 0
		OgvS= 0
		for m in self.data:
			if m[0] is given:
				s+= 1
				if m[1] is output:
					OgvS +=1
		num = 1+ OgvS
		den= s+8
		ans= float(num) / float(den)
		self.letterEm[given][output]= round(ans,3)
		return round(ans,3)

	def transition(self, next, now):
		occur= 0
		nexter= 0
		for m in range(0, len(self.data)):
			if data[m][0] is now:
				occur +=1
				#Protect from indexing outside of array
				try:
					if self.data[m+1][0] is next:
						nexter +=1
				except IndexError:
					pass
		num = 1 + nexter
		den = 26 + occur
		ans = float(num) / float(den)
		self.letterTr[now][next]= round(ans, 3)
		return round(ans, 3)
		
	def printer(self):
		print "For Emission Probabilities:\n\n"
		results = []
		for k in self.letterEm.keys():
			for ns, value in self.letterEm[k].items():
				strn = "P("+ns+"|"+k+") = " + str(value)
				results.append(strn)
		for m in sorted(Results):
			print m
		print "/n/n For Transition Probabilities:/n/n"
		results = []
		for k in self.letterTr.keys():
			for ns, value in self.letterTr[k].items():
				strn = "P("+ns+"|"+k+") = " + str(value)
				results.append(strn)
		for m in sorted(Results):
			print m
		
		print "\n\nMarginal Values: \n\n"
		for k in self.letterInit.keys():
			print "initial marginal for", k+":", self.letterInit[k]
 


filename= 'typos20.data'
typos= open(filename, 'r')
data= []
#Put all information into a array with tuples
file= typos.readlines()
for line in file:
	if line[0] is not '_':
		data.append((line[0], line[2]))
markov= HMM(data)
print markov.emission('n', 'j')
print markov.letterEm['j']['n']
for x, ev in data:
	markov.emission(ev, x)
for next in range(97, 123):
	for now in range(97, 123):
		markov.letterTr(chr(next),chr(now))
	
if __name__ == '__main__':
	
	sys.stdout = open('output.txt', 'w')

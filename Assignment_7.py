samples= [0.82,	0.56,	0.08,	0.81,	0.34,	0.22, 0.37, 0.99,	0.55,	0.61,	0.31,	0.66,	0.28,	1.0,	0.95, 0.71, 0.14,	0.1,	1.0,	0.71,	0.1,	0.6,	0.64,	0.73, 0.39, 0.03,	0.99,	1.0,	0.97,	0.54, 	0.8, 0.97, 0.07,	0.69, 0.43, 0.29,	0.61,	0.03,	0.13,	0.14,	0.13,	0.4, 0.94, 0.19, 0.6, 0.68,	0.36,	0.67,	0.12,	0.38, 0.42,	0.81, 0.0,	0.2, 0.85, 0.01,	0.55,	0.3,	0.3,	0.11, 0.83,	0.96, 0.41, 0.65, 0.29,	0.4,	0.54,	0.23,	0.74,	0.65,	0.38, 0.41,	0.82, 0.08, 0.39,	0.97,	0.95,	0.01,	0.62,	0.32, 0.56, 0.68, 0.32, 0.27,	0.77, 0.74, 0.79, 0.11, 0.29, 0.69, 0.99, 0.79, 0.21,	0.2,	0.43,	0.81, 0.9,	0.0,	0.91,	0.01]
odb = 0
clouds= []
sprinkles= []
rain= []
wet= []
ghost=0
face= 0
killa1= 0
killa2= 0
#Prob 1
for k in samples:
	if odb is 0:
		if k  < 0.5: #P(c)= 0.5
			clouds.append(True)
		else:
			clouds.append(False)
	if odb is 1:
		if k  <0.3: #P(s)= 0.3
			sprinkles.append(True)
		else:
			sprinkles.append(False)
	if odb is 2:
		if k  < 0.5: #P(r)= 0.5
			rain.append(True)
		else:
			rain.append(False)
	if odb is 3:
		if k  < 0.6: #P(w)= 0.6
			wet.append(True)
		else:
			wet.append(False)		
	odb += 1
	odb= odb% 5

for z in range(len(clouds)):
	if rain[z] and clouds[z]:
		ghost +=1
	if wet[z] and sprinkles[z]:
		face += 1
	if wet[z] and clouds[z]:
		killa1 += 1
		if sprinkles[z]:
			killa2 += 1

	
probC= float(clouds.count(True))/ float(len(clouds))
pCgvR= float(ghost)/ float(rain.count(True))
pSgvW= float(face)/ float(wet.count(True))
pSgvCW= float(killa2)/ float(killa1)
print killa2
print killa1
print wet
print len(clouds)
print "1.A the probability of C= true is ", probC
print "1.b the probability of c= t | r = t", pCgvR
print "1.c the probability of s=t | w= t", pSgvW
print "1.d the probability of s= t | c = t, w= t", pSgvCW

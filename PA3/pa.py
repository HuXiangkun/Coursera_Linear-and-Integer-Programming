from __future__ import division
import sys

global m
m = 0
global n
n = 0
global B
B = []
global N
N = []
global b
b = []
global a
a = []
global c
c = []
global z
z = 0

global isPivotDone
isPivotDone = False
global isUnbounded
isUnbounded = False
global isInfeasible
isInfeasible = False

#read file
def readFile():
	fileName = sys.argv[1]
	f = open(fileName,"r")

	global m
	global n
	global B
	global N
	global b
	global a
	global c
	global z

	line = f.readline().split(" ")
	m = int(line[0])
	n = int(line[1])
	a = [[0 for x in range(n)] for x in range(m)]

	line = f.readline().strip().split(" ")

	for i in range(len(line)):
		B.append(int(line[i]))
        
	line = f.readline().strip().split(" ")
	
	for i in range(len(line)):
		N.append(int(line[i]))

	line = f.readline().strip().split(" ")
	
	for i in range(len(line)):
		b.append(float(line[i]))
    
	for i in range(m):
		line = f.readline().strip().split(" ")
		for j in range(n):
			a[i][j] = float(line[j])

	line = f.readline().strip().split(" ")
	
	c = []
	for i in range(len(line)):
		c.append(float(line[i]))
	z = c[0]
	c = c[1:]
#pivot
def pivot():
	#select entering variable
	global m
	global n
	global B
	global N
	global b
	global a
	global c
	global z
	global isPivotDone
	global isUnbounded
	global isInfeasible

	enterings = []
	enteringIndexes = []

	isCompelte = True
	for i in range(n):
		
		if c[i]>0:
			isCompelte = False
			isAllPositive = True
			for j in range(m):
				if a[j][i]<0:
					isAllPositive = False
			if isAllPositive!=True:
				enterings.append(i)
				enteringIndexes.append(N[i])
	if isCompelte: #pivot compelte
		isPivotDone = True
		return

	if len(enterings) == 0:	#unbounded
		isUnbounded = True
		isPivotDone = True
		return

	enteringIndex = min(enteringIndexes)
	entering = enterings[enteringIndexes.index(enteringIndex)]

	#print enteringIndex  #the index of entering variable

	#select leaving variable
	leavingIndexes = []
	values = []
	for i in range(m):
		if a[i][entering]<0:
			values.append(b[i]/abs(a[i][entering]))
			leavingIndexes.append(i)

	minValue = min(values)
	leavings = []
	for i in range(len(values)):
		if minValue == values[i]:
			leavings.append(B[leavingIndexes[i]])
        
	leavingIndex = min(leavings)
	#print leavingIndex        #the index of leaving variable

	#compute z
	i = B.index(leavingIndex)
	j = N.index(enteringIndex)
	z = z + abs(c[j]*b[i]/a[i][j])

	#print z   #the objective value in next dictionary

	#compute new B, b, N a and c
	indexOfLeavingInArrary = B.index(leavingIndex)
	indexOfEnteringInArray = N.index(enteringIndex)
	#change B, b, a in the row of leaving variable
	B[indexOfLeavingInArrary] = enteringIndex
	N[indexOfEnteringInArray] = leavingIndex
	b[indexOfLeavingInArrary] = -b[indexOfLeavingInArrary]/a[indexOfLeavingInArrary][indexOfEnteringInArray]
	
	for i in range(n):
		if i != indexOfEnteringInArray:
			a[indexOfLeavingInArrary][i] = -a[indexOfLeavingInArrary][i]/a[indexOfLeavingInArrary][indexOfEnteringInArray]
	a[indexOfLeavingInArrary][indexOfEnteringInArray] = 1/a[indexOfLeavingInArrary][indexOfEnteringInArray]
	#change b, a not in the row of leaving variable
	for i in range(m):
		if i != indexOfLeavingInArrary:
			b[i] = b[i] + a[i][indexOfEnteringInArray]*b[indexOfLeavingInArrary]
			for j in range(n):
				if j != indexOfEnteringInArray:
					a[i][j] = a[i][j] + a[i][indexOfEnteringInArray]*a[indexOfLeavingInArrary][j]
			a[i][indexOfEnteringInArray] = a[i][indexOfEnteringInArray]*a[indexOfLeavingInArrary][indexOfEnteringInArray]
	#change c
	for i in range(n):
		if i != indexOfEnteringInArray:
			c[i] = c[i] + c[indexOfEnteringInArray]*a[indexOfLeavingInArrary][i]
	c[indexOfEnteringInArray] = c[indexOfEnteringInArray]*a[indexOfLeavingInArrary][indexOfEnteringInArray]
#initialize
def initialize():
	global m
	global n
	global B
	global N
	global b
	global a
	global c
	global z

	isNeedInit = False
	for i in range(m):
		if b[i]<0:
			isNeedInit = True
			break
	if isNeedInit == False:
		return
	#save the origin problem
	mTemp = m
	nTemp = n
	BTemp = B
	NTemp = N
	bTemp = b
	aTemp = a
	cTemp = c
	zTemp = z

	n = mTemp
	m = nTemp
	b = [1 for i in range(m)]
	a = [[-r[col] for r in a] for col in range(len(a[0]))]
	N = [BTemp[i] for i in range(n)]
	B = [NTemp[i] for i in range(m)]
	c = [-i for i in bTemp]
	z = 0

	#solve the dual
	global isPivotDone
	global isUnbounded
	global isInfeasible
	while isPivotDone == False:
		pivot()
	if isUnbounded == True:
		print "Infeasible"
		sys.exit(0)
	isPivotDone = False
	isUnbounded = False
	isInfeasible = False
	#conversion to the primal dictionary
	z = -z
	cT = c #temp variable
	c = [-i for i in b]
	b = [-i for i in cT]
	m = mTemp
	n = nTemp
	a = [[-r[col] for r in a] for col in range(len(a[0]))]
	BT = B #temp variable
	B = [N[i] for i in range(m)]
	N = [BT[i] for i in range(n)]
	#restoring objective
	zNew = 0
	cNew = [0 for i in range(n)]
	for i in range(n):
		if NTemp[i] in B:
			index = B.index(NTemp[i])
			zNew = zNew + cTemp[i]*b[index]
			cNew = [cTemp[i]*a[index][j]+cNew[j] for j in range(len(a[index]))]
	for i in range(n):
		if NTemp[i] in N:
			index = N.index(NTemp[i])
			cNew[index] = cNew[index] + cTemp[index]

	z = zNew
	c = cNew


def main():
	global isPivotDone
	readFile()
	initialize()
	while isPivotDone == False:
		pivot()
	print z



if __name__ == '__main__':
	main()





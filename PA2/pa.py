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

	enterings = []
	enteringIndexes = []
	print n
	for i in range(n):
		if c[i]>0:
			isAllPositive = True
			for j in range(m):
				if a[j][i]<0:
					isAllPositive = False
			if isAllPositive!=True:
				enterings.append(i)
				enteringIndexes.append(N[i])

	if len(enterings) == 0:
		print "UNBOUNDED"
		sys.exit(0)

	enteringIndex = min(enteringIndexes)
	entering = enterings[enteringIndexes.index(enteringIndex)]

	print enteringIndex

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
        
	leaving = min(leavings)
	print leaving

	#compute z
	i = B.index(leaving)
	j = N.index(enteringIndex)
	z = z + abs(c[j]*b[i]/a[i][j])
	print z

def main():
	readFile()
	while True:
		pivot()



if __name__ == '__main__':
	main()





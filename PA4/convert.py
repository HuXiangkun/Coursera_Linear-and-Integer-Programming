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

def convertToMath():
	for i in range(n):
		print "var x%s integer;" % (i+1);

	obj = "%s" % z
	for i in range(n):
		if c[i]>=0:
			obj = obj + "+%s*x%s" % (int(c[i]),i+1)
		else:
			obj = obj + "%s*x%s" % (int(c[i]),i+1)
	print "maximize obj:%s;" % (obj)

	for i in range(m):
		constrain = "c%s: " % (i+1)
		for j in range(n):
			if a[i][j]>0:
				constrain = constrain + "%s*x%s" % (int(-a[i][j]),j+1)
			elif a[i][j]<0:
				constrain = constrain + "+%s*x%s" % (int(-a[i][j]),j+1)
			else:
				constrain = constrain + "+%s*x%s" % (int(a[i][j]),j+1)
		constrain = constrain + "<=%s;" % (int(b[i]))
		print constrain
	for i in range(n):
		print "c%s: x%s>=0;" % (i+m+1,i+1)

	print "solve;"
	print "display %s;" % (obj)
	print "end;"


def main():
	readFile()
	convertToMath()



if __name__ == '__main__':
	main()





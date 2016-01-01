#!/usr/bin/python2

import numpy as np
import matplotlib.pyplot as plt

def update_weights(point, weight, target):
	weight[0] = weight[0] + target*point[0]
	weight[1] = weight[1] + target*point[1]
	weight[2] = weight[2] + target
	return weight

def calc_output(point, weight):
	return np.sign(weight[1]*point[1]+weight[0]*point[0] + weight[2])

def calc_target(point):
	return np.sign(a[1]*point[1] + a[0]*point[0] + a[2])

#what is the convergence criterion?


#number of points
numPoints = 100
#correct answer
a = [1.0, 2.0,3.0]

#initial weight
weights = np.random.randn(3,)
print weights

#initialize points
points = []
for i in range(numPoints):
	points.append(np.random.randn(2,))
points = np.array(points)
print points

target = [calc_target(points[i]) for i in xrange(len(points))]
print target

pOnes = np.ones(numPoints)
mOnes = np.empty(numPoints)
mOnes.fill(-1.0)

onLine = [[-1.0, -1.0],[0.0, -3.0/2.0],[3.0,0.0]]


plus = points[np.equal(target , pOnes)]
minus = points[np.equal(target, mOnes)]

#plt.scatter(minus[:,0], minus[:,1], c='b')
#plt.scatter(plus[:,0], plus[:,1], c='r')
plt.plot(onLine, c='k',linestyle='dashed')
plt.show()

# output = [calc_output(points[i], weights) for i in xrange(len(points))]
# print output


# maxIterations = 100
# iteration = 0

# while(iteration < maxIterations):
# 	while((np.array_equal(output,target))!=True):
# 		mismatch = points[np.not_equal(output,target)]
# 		i = np.random.randint(0, len(mismatch))
# 		tget = calc_target(mismatch[i])
# 		update_weights(mismatch[i],weights, tget)
# 		print weights
# 		output = [calc_output(points[i], weights) for i in xrange(len(points))]



# print "Out of loop"








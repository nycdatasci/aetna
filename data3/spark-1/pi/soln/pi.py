import random

def rand_pair(x): # generate a random number pair 
    return (random.random(), random.random())
def in_circle(p): # test if p is within the circle
    x, y = p      # same as x = p[0], y = p[1]
    return x*x + y*y < 1

samples = 10000
count_needles = sc.parallelize(samples * [1])
points = count_needles.map(rand_pair)
point_in_circle = points.filter(in_circle).count()

print 4.0 * point_in_circle / samples

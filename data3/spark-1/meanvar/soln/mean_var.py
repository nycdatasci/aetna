
def mean_rating(rdd):
    vals = rdd.map(lambda x: (x, 1))\
               .reduce(lambda x,y: (x[0]+y[0], x[1]+y[1]))
    return vals[0] / vals[1]

def var_rating(rdd):
    mu = mean_rating(rdd)
    vals = rdd.map(lambda x: ((x - mu)**2, 1)) \
               .reduce(lambda x, y: (x[0]+y[0], x[1]+y[1]))
    return vals[0] / vals[1]

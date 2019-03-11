def contribs(x):
    links = x[1][0].split()
    out_d = len(links)
    for link in links:
        yield link, x[1][1]/out_d

rank_raw = [('a',.25), ('b', .25), ('c', .25), ('d', .25)] # initial ranks
link_raw = [('a', 'b c d'), ('b', 'a c'), ('c', 'd'), ('d', 'a b')]
ranks = sc.parallelize(rank_raw)
links = sc.parallelize(link_raw)
links.cache()

for i in range(10):
    # your code goes here:
    # update ranks in each iteration

print ranks.collect() 

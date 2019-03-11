txt = sc.textFile("genesis.txt")
wc = txt.flatMap(lambda line: line.split()) \
        .map(lambda word: (word, 1)) \
        .reduceByKey(lambda a, b: a + b)
fc = wc.map(lambda w: (w[1], 1)) \
       .reduceByKey(lambda a, b: a + b)
print fc.take(10)

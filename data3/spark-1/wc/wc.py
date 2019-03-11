txt = sc.textFile("genesis.txt")
wc = txt.flatMap(lambda line: line.split()) \
        .map(lambda word: (word, 1)) \
        .reduceByKey(lambda a, b: a+b)
# print wc.take(10)
wc.saveAsTextFile('spark-wc')

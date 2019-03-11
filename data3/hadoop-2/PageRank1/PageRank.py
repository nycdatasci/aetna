#!/usr/bin/env python

import os
from sys import argv

script, input_file, iters = argv
iters = int(iters)
streaming = '''hadoop jar $HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming-*.jar \
-files PageRankMap.py,PageRankReduce.py \
-input %s \
-output PageRankOutput \
-mapper PageRankMap.py \
-reducer PageRankReduce.py
''' % input_file

get_pop = 'hadoop fs -get PageRankOutput/part-00000'
rm_output = 'hadoop fs -rm -R PageRankOutput'
update_pop_local = 'mv part-00000 pop_table'
rm_pop_table = 'hadoop fs -rm pop_table'
update_pop_hdfs = 'hadoop fs -put pop_table'

os.system("hadoop fs -put %s" % input_file)

for i in range(iters):
    os.system(streaming)
    os.system(get_pop)
    os.system(rm_output)
    os.system(update_pop_local)
    os.system(rm_pop_table)
    os.system(update_pop_hdfs)
    print("%d th iteration:" % (i+1))
    os.system("cat pop_table")

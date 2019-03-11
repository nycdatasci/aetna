#hadoop fs -put input.txt /wordcount
hadoop jar $HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming-*.jar \
  -input input.txt \
  -output output \
  -mapper map.py \
  -reducer reduce.py

#hadoop fs -put input.txt /wordcount
hadoop jar $HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming-*.jar \
  -files map.py,reduce.py \
  -input input.txt \
  -output output \
  -mapper map.py \
  -combiner reduce.py \
  -reducer reduce.py

hadoop jar $HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming-*.jar \
  -input input.txt \
  -output output \
  -mapper map.py \
  -reducer reduce.py
hadoop jar $HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming-*.jar \
  -input output/part-00000 \
  -output output2 \
  -mapper map2.py \
  -reducer reduce.py

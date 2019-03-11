hadoop jar $HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming-*.jar \
  -input input.txt \
  -output output0 \
  -mapper wc_map.py \
  -reducer reduce.py
hadoop jar $HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming-*.jar \
  -input output0/part-00000 \
  -output output \
  -mapper freq_map.py \
  -reducer reduce.py

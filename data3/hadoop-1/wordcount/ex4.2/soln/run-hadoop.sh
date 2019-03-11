hadoop jar $HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming-*.jar \
  -files map.py,reduce.py \
  -input input.txt \
  -output output \
  -mapper map.py \
  -reducer reduce.py
hadoop jar $HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming-*.jar \
  -files map2.py,reduce.py \
  -input output/part-00000 \
  -output output2 \
  -mapper map2.py \
  -reducer reduce.py

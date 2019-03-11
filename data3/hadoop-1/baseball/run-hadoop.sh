hadoop jar $HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming-*.jar \
  -input hitters.csv \
  -output output \
  -mapper map.py \
  -reducer reduce.py

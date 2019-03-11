hadoop jar $HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming-*.jar \
  -files map.py,reduce.py \
  -input hitters.csv \
  -output output \
  -mapper map.py \
  -reducer reduce.py

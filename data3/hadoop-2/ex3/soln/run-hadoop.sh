hadoop jar $HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming-*.jar \
  -files ex3_mapper.py,ex3_reducer.py \
  -input genesis.txt\
  -output output_ex3 \
  -mapper ex3_mapper.py \
  -reducer ex3_reducer.py

hadoop jar $HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming-*.jar \
  -files ex1_mapper.py,ex1_reducer.py \
  -input reviews.csv\
  -output output_ex1 \
  -mapper ex1_mapper.py \
  -reducer ex1_reducer.py

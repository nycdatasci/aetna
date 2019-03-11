#hadoop fs -mkdir wordcount
#hadoop fs -put bible.txt wordcount
hadoop jar $HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming-*.jar \
  -files ex2_mapper.py,ex2_combiner.py,ex2_reducer.py \
  -input reviews.csv \
  -output output_ex2 \
  -mapper ex2_mapper.py \
  -reducer ex2_reducer.py \
  -combiner ex2_combiner.py
#hadoop fs -cat wordcount/bible_count/*

#!/bin/bash
for i in hospital-data.csv diagcodemap.csv; do
    if ! $(hdfs dfs -test -d $i 2>/dev/null) ; then
        echo "Adding data $i to hdfs"
        hdfs dfs -put /data3/$i 2>/dev/null;
    fi
done

echo "Adding tables to default database in Hive"
hive -f /data3/hive-create-tables.hql 2>/dev/null
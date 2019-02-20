admits = LOAD 'hospital_admits.csv'
         USING PigStorage(',')
         AS (facility:CHARARRAY, age:CHARARRAY,
             gender:CHARARRAY, lengthofstay:INT);

longstay = FILTER admits BY lengthofstay >= 5;
by_age = GROUP longstay BY age;
avg_longstay_by_age = FOREACH by_age
     GENERATE group, AVG(longstay.lengthofstay);
ILLUSTRATE avg_longstay_by_age;


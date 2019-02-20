#!/bin/bash

while read line
do
  lengthofstay=$(echo "$line" | cut -f4)
  totalcharges=$(echo "$line" | cut -f9)
  perday=$( echo $totalcharges $lengthofstay \
            | awk '{ print $1/$2 }' )
  i=$lengthofstay
  while (( i > 0 ))
  do
    echo "$line" | sed "s/\t[^\t]*$/\t$perday/"
    i=$((i-1))
  done
done

sed 's/[^a-zA-Z]\{1,\}/\
   /g' file_name | # remove non-alphabet chars
   sed '/^$/d' |          # delete blank lines
   sort | uniq -c |       # sort and count
   sort -n                # sort by frequencies

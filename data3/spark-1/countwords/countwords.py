
def countwords(file):
    # your code goes here
    # 1. create an RDD using sc.textFile(file)
    # 2. do map operation to count the number of words on each line
    #    lambda line: len(line.split()) will do the job
    # 3. do reduce operation to sum up the numbers and return it

def countwords_ch_1(file):
    # your code goes here
    # apply filter to select lines begin with '1:'
    pass
    

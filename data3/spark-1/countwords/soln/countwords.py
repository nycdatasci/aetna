
def countwords(file):
   txt = sc.textFile(file)
   counts = txt.map(lambda line: len(line.split()))
   return counts.reduce(lambda x, y: x+y)

def countwords_ch_1(file):
   txt = sc.textFile(file).filter(lambda line: line[:2] == '1:')
   counts = txt.map(lambda line: len(line.split()))
   return counts.reduce(lambda x, y: x+y)

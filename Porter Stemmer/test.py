# import porternew
import PorterStemmer
lines = open('voc.txt').read().splitlines()

for line in lines:
    # print(porternew.process(line))
    if len(line) > 2:
        print(PorterStemmer.process(line))                        
    else:            
        print(line)

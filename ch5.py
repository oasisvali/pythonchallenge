import sys
import re
import pickle

filename = "banner.p"

f = open(filename,'r')

x = pickle.load(f)

for elem in x:
  for elem2 in elem:
    sys.stdout.write(elem2[0]*elem2[1])
  print

f.close()

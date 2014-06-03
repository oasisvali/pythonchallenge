import re

filename = "equality.html"

f = open(filename,'r')
dump = f.read()
results = re.findall(r'<!--(.*?)-->',dump,re.DOTALL)

print results[1]

chrlist = re.findall(r'[a-z][A-Z]{3}([a-z])[A-Z]{3}[a-z]',results[1])

chrdict = {}

for charac in chrlist:
  if charac in chrdict:
    chrdict[charac] +=1
  else:
    chrdict[charac] = 1

print ''.join(chrdict.keys()+['i','l'])

f.close()

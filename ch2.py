import re

filename = "ocr.html"

f = open(filename,'r')
dump = f.read()
results = re.findall(r'<!--(.*?)-->',dump,re.DOTALL)

print len(results)

chrdict = {}

for charac in results[2]:
  if charac in chrdict:
    chrdict[charac] += 1
  else:
    chrdict[charac] = 1

print chrdict

f.close()

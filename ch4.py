import urllib2
import re

url = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=8022'

usock = urllib2.urlopen(url)
data = usock.read()
usock.close()
print data

contin = True

i=0
while (i<400):
  matchO = re.search(r'nothing is (\d+)$',data)
  url = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing='+matchO.group(1)
  usock = urllib2.urlopen(url)
  data = usock.read()
  print data
  usock.close()
  i+=1

#print data

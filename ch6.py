import zipfile
import re

f = open('ch6.dat','w')

file = zipfile.ZipFile('channel.zip','r')

res = {'Empty':0}
strr = ''



dat = '90052.txt'
while dat:

  info = file.getinfo(dat)
  dat = file.read(dat)
  print dat
  if len(info.comment)>0:
    strr += info.comment
  matchObj = re.search(r'nothing is (\d+)',dat,re.S|re.I)
  try:
    dat = matchObj.group(1)
  except:
    break
  dat = dat+'.txt'


f.write(strr)
f.close()

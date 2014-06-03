from PIL import Image as im

def chunks(l,n):
  retlist = []
  for i in xrange(0,len(l),n):
    tmplist = l[i:i+n]
    retlist.append(tmplist)
  return retlist

if __name__ == '__main__':

  img = im.open('oxygen.png')

  li = list(img.getdata())

  li = chunks(li,629)
  print len(li)
  print len(li[94])
  print len(li[0])

  i = []
  for row in i:
    if li[i]==li[i-1]: 
      if li[i]==li[i-2]:
        if li[i]==li[i-3]:
          if li[i]==li[i-4]:
            if li[i]==li[i-5]:
              print 'match found at row',i
              print
              print row
              break
    i+=1
  print 'not'
  finlist = []
  for pixel in li[45]:
    finlist += [pixel[0]]
  print len(finlist)
  endlist = [finlist[0]]
  rptchck = 0
  for i in range(625):
    if finlist[i] != endlist[-1]:
      endlist += [finlist[i]]
      rptchck = 0
    else:
      rptchck += 1

    if rptchck>10:
      endlist+= [finlist[i]]
      rptchck = 0
    if endlist[-1] == 93:
      break
#  endlist = [105,110,116,101,103,114,105,116,121]
  retlist= ""
  for chrr in endlist:
    retlist += chr(chrr)
  print retlist
  f = open('ch7.dat','w')

  f.write(retlist)
  f.close()

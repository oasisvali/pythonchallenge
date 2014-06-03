import re
import PIL.Image as Image
import PIL.ImageDraw as ID

def tolist(string):
  retlist = []
  num = ''
  for char in string:
    if char == '\n':
      continue
    elif char == ',':
      retlist+=[int(num)]
      num = ''
    else:
      num+=char
  retlist+=[int(num)]
  return retlist

if __name__=='__main__':
  f=open('ch9.html','r')

  html = f.read()

  f.close()

  matchObj = re.search(r'<!--\nfirst\+second=\?\n\nfirst:\n(.*?)\n\nsecond:\n(.*?)\n\n-->',html,re.S)

  first = matchObj.group(1)
  second = matchObj.group(2)

  first = tolist(first)
  second = tolist(second)

  print len(first)
  print len(second)

  for elem in second:
    first.append(elem)
  
  print len(first)

  im = Image.open('good.png')
  draw = ID.Draw(im)
  draw.polygon(first,fill=256)
  # draw.polygon(second,fill=256)
  del draw
  im.show()

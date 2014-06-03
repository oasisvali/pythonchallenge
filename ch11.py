from PIL import Image as im
from ch7 import chunks

if __name__ == '__main__':

  img = im.open('cave.png')

  li = list(img.getdata())
  print img.mode
  finlist = []
  orig_list = li
  li = chunks(li,640)
  rctr = 0
  for row in li:
    ctr = 0
    for pix in row:
      if (ctr%2 != 0) and (rctr%2!=0):  #odd if odd row
        finlist += [pix]
      elif (ctr%2 == 0) and (rctr%2==0):
        finlist += [pix]
      ctr += 1
    rctr+=1
  
  fim = im.new('RGB',(320,480))
  fim.putdata(finlist)
  fim.show()


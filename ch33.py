from collections import defaultdict
from pprint import pprint
from PIL import Image
import operator
import math


def perfect_sq(n):
  return n == int(math.sqrt(n)) ** 2

if __name__ == '__main__':
  img = Image.open('beer2.png')
  # print img.mode
  # print img.size

  imgdata = list(img.getdata())
  colors = img.getcolors()[::-1]
  print colors

  for j in xrange(0,len(colors),2):
    print colors[j][1]
    new_imgdata = list(imgdata)
    imgdata = []
    for i in xrange(len(new_imgdata)):
      if new_imgdata[i] != colors[j][1]:
        if new_imgdata[i] != colors[j+1][1]:
          #only append if the current pix is not a part of 2 consecutive colors
          imgdata.append(new_imgdata[i])
        new_imgdata[i] = 0
      else:
        new_imgdata[i] = 255

    print(len(imgdata))
    dim = int(math.sqrt(len(new_imgdata)))
    print dim*dim
    print len(new_imgdata)
    new_img = Image.new(img.mode, (dim,dim))
    new_img.putdata(new_imgdata)
    new_img.show()
    # raw_input()
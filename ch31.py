from decimal import Decimal
from PIL import Image

H = 480
W = 640

def mine():
  orig_img = Image.open('mandelbrot.gif')

  print orig_img.mode
  pal = orig_img.getpalette()
  #orignal image needs to be vertically flipped to be right orientation for comparison with our mandelbrot img
  orig_img = orig_img.transpose(Image.FLIP_TOP_BOTTOM)

  # draw our own mandelbrot fractal

  # starting drawing area - left="0.34" top="0.57" width="0.036" height="0.027"
  height = 0.027
  width = 0.036
  x_start = 0.34
  y_start = 0.57  #html top means bottom!

  maxIt = 128 # max iterations allowed

  # image size
  imgx = W
  imgy = H

  image = Image.new("P", (imgx, imgy))
  image.putpalette(pal)

  diffs = []
  diffvals = []
  image_data = []

  for y in xrange(imgy):
    # print y
    cy = float(y) * height / float(imgy) + y_start
    for x in xrange(imgx):
      cx = float(x) * width / float(imgx) + x_start

      c = complex(cx, cy)
      z = complex(0.0)

      for i in xrange(1, maxIt+1):
        if abs(z) >= 2:
          break
        z = z * z + c

      #the closer i is to maxIt, the better this current point is a part of the mandelbrot set

      iterations = i-2
      image_data.append(iterations)

      orig = orig_img.getpixel((x,y))
      diff = orig-iterations

      if abs(diff) > 0 and orig != 127:   # orig  = 127 pixels are just wierd
        diffs.append(diff)
        diffvals.append(iterations)


  image.putdata(image_data)
  image.show()
  print len(diffs)
  # print diffs[:100]
  # print diffvals[:100]
  # print ''.join(chr(x) for x in diffvals)



if __name__ == '__main__':

  # other()

  mine()
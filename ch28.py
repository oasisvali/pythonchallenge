from PIL import Image

if __name__ == '__main__':
  img = Image.open('bell.png')
  print img.mode
  img = list(img.getdata())
  # print len(img)
  # print img[:100]

  green_channel = [x[1] for x in img]

  dat = []
  for i in xrange(0,len(green_channel),2):
    if abs(green_channel[i] - green_channel[i+1]) != 42:
      dat.append(abs(green_channel[i] - green_channel[i+1]))


  print len(dat)
  print ''.join(chr(x) for x in dat)

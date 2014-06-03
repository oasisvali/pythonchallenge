import csv
from PIL import Image
from PIL.Image import FLIP_TOP_BOTTOM

def get_n(x,i):
  return ('%.6f'%x[i])[5] + ('%.6f'%x[i+1])[5] + ('%.6f'%x[i+2])[6]

if __name__ == '__main__':
  imgdat = []

  with open('yankeedoodle.csv', 'rb') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')

    for row in reader:
      for val in row:
        if len(val) > 0:
          imgdat.append(float(val))

  # print len(imgdat)
  # print imgdat[:100]

  # fim = Image.new('RGB',(53, 139))
  # fim.putdata([(int(i*255),int(i*255),int(i*255)) for i in imgdat])
  # fim = fim.rotate(90)
  # fim = fim.transpose(FLIP_TOP_BOTTOM)
  # fim.show()

  sol = []
  for i in xrange(0,len(imgdat)-2,3):
    sol.append(int(get_n(imgdat, i)))
  print ''.join(chr(x) for x in sol)
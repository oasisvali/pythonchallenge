from itertools import izip
import keyword
from PIL import Image
import bz2


def show_string(string):
  return
  print len(string)
  print string[:100]
  print string[:100].encode('hex')


def calc_diff(dat1, dat2):
  assert len(dat1) == len(dat2)

  #first align the data streams
  dat1 = dat1[1:]
  dat2 = dat2[:-1]

  difference = []
  diff_indexes = []
  for i in xrange(len(dat1)):
    if dat1[i] != dat2[i]:
      difference.append(dat1[i])
      diff_indexes.append(i)

  return difference, diff_indexes


if __name__ == '__main__':

  img = Image.open('zigzag.gif')
  # print img.mode

  pal = img.getpalette()
  pal_cmp = pal[::3]
  # print len(pal_cmp)

  img = list(img.getdata())

  dat = ''.join(chr(x) for x in img)
  show_string(dat)

  img_mapped = list(pal_cmp[i] for i in img)

  dat_mapped = ''.join(chr(x) for x in img_mapped)
  show_string(dat_mapped)

  difference, diff_indexes = calc_diff(dat, dat_mapped)
  dat_difference = ''.join(difference)
  show_string(dat_difference)

  diff_txt = bz2.decompress(dat_difference)
  words = diff_txt.split()
  not_kw = {word for word in words if not keyword.iskeyword(word)}

  print not_kw

  new_img = [(255,255,255) for i in xrange(320*270)]
  for index in diff_indexes:
    new_img[index] = (50,50,50)

  fim = Image.new('RGB',(320, 270))
  fim.putdata(new_img)
  fim.show()



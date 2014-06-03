from itertools import izip_longest, izip, chain
from pprint import pprint
import wave
from PIL import Image
import requests
from requests.auth import HTTPBasicAuth
from ch7 import chunks

DIR = './ch25_files/'
URL = 'http://www.pythonchallenge.com/pc/hex/lake{0}.wav'
NFRAMES = 10800

def downloadFiles():
  i = 1
  while True:
    r = requests.get(URL.format(i), stream=True, auth=HTTPBasicAuth('butter', 'fly'))
    # print r.status_code
    # print r.reason
    if r.status_code == 200:
      with open(DIR + str(i) + '.wav', 'wb') as f:
          for chunk in r.iter_content():
              f.write(chunk)
    else:
      print 'Downloaded ', i-1, 'files'
      return
    i+=1


def pixify(dat):
  assert len(dat) % 3 == 0

  ret = []
  args = [iter(dat)] * 3
  for pix in izip_longest(*args, fillvalue=0):
    ret.append(pix)
  return ret


def place_piece(dat, new_img, i):
  assert len(dat) == 60
  offset_x = (i%5)*60
  offset_y = (i/5)*60

  for i, off_i in izip(xrange(60), xrange(offset_y,offset_y+60)):
    for j, off_j in izip(xrange(60), xrange(offset_x, offset_x+60)):
      # off_i, off_j gives coordinates where the dat must be placed in new_img
        new_img[off_i][off_j] = dat[i][j]



def solveJigsaw():
  wavdata = []
  for i in xrange(1,26):
    filename = DIR + str(i) + '.wav'
    wav = wave.open(filename, 'rb')
    wavdata.append(wav.readframes(NFRAMES))
    wav.close()


  # now break up the data streams into pix sized chunks and draw the img
  new_img = list(list(() for i in xrange(300)) for i in xrange(300))
  for i, wav in enumerate(wavdata):
    dat = list(ord(x) for x in wav)
    dat = pixify(dat)
    dat = chunks(dat,60)
    place_piece(dat, new_img, i)

  print len(new_img)
  print len(new_img[0])
  print new_img[0][0]
  new_img = list(chain(*new_img))
  fim = Image.new('RGB',(60*5,60*5))
  fim.putdata(new_img)
  fim.show()

if __name__ == '__main__':

  # downloadFiles()

  solveJigsaw()
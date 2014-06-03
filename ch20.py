from PIL import Image as im
import requests
from pprint import pprint
from requests.auth import HTTPBasicAuth
import zlib
import StringIO
from zipfile import ZipFile

MAX_RANGE = 2123456789

msg = 'esrever ni emankcin wen ruoy si drowssap eht'
password = 'invader'[::-1]
hiding = 1152983631

if __name__ == '__main__':

  # valid_offsets = []
  # messages = []
  # for i in xrange(MAX_RANGE - 2 - len(msg), MAX_RANGE*2):
  #   print i
  #   r = requests.get('http://www.pythonchallenge.com/pc/hex/unreal.jpg', headers={'Range': 'bytes={0}-{1}'.format(i, i+1)}, auth=HTTPBasicAuth('butter', 'fly'))
  #   if r.status_code == 206:
  #     valid_offsets.append(i)
  #     messages.append(r.text)
  #     print r.text

  # pprint(messages)

  # r = requests.get('http://www.pythonchallenge.com/pc/hex/unreal.jpg', headers={'Range': 'bytes=1152983631-'}, auth=HTTPBasicAuth('butter', 'fly'))

  # print r.status_code
  # print r.reason
  # dat = r.content
  # print dat[:100]
  # print len(dat)
  
  # f = open('unreal.zip', 'wb')
  # f.write(dat)
  # f.close()

  f = open('unreal.zip', 'rb')
  dat = f.read()
  f.close()
  print dat[:100]
  print len(dat)

  z = ZipFile(StringIO.StringIO(dat))
  print z.namelist()
  z.setpassword(password)
  z.extractall(path='./ch21_files/')
  z.close()





  

  


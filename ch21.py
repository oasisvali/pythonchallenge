import zlib
from pprint import pprint
import bz2

PACK = './ch21_files/package.pack'

if __name__ == '__main__':

  f = open(PACK, 'rb')
  data = f.read()
  f.close()

  ctr = 1

  log = ''

  while True:
    ctr += 1
    if data[:10].encode("hex")[:4] == '789c':
      print data[:10].encode("hex")
      data = zlib.decompress(data)
      log += '1'
    elif data[:3] == 'BZh':
      print data[:10]
      data = bz2.decompress(data)
      log += '2'
    elif data[-10:][::-1].encode("hex")[:4] == '789c':
      data = data[::-1]
      print data[:10].encode("hex")
      data = zlib.decompress(data)
      log += '3'
    elif data[::-1][:3] == 'BZh':
      data = data[::-1]
      print data[:10]
      data = bz2.decompress(data)
      log += '4'
    else:
      print '\nBREAKING\n'
      
      print data[::-1]
      break

  # print log
  # print len(log)

  # disp = log.split('1')
  # pprint(disp)
  # disp = log.split('2')
  # pprint(disp)
  log = log.replace('1', ' ')
  disp = log.split('3')
  pprint(disp)
  # disp = log.split('4')
  # pprint(disp)





  

  


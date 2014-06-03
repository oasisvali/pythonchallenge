import hashlib
import pickle
from zipfile import ZipFile
from PIL import Image as im
import sys
from StringIO import StringIO
from ch7 import chunks
import itertools

EMAIL_MD5 = 'bbb8b499a0eef99b52c7f13f4e78c24b'
GIF_MD5 = '6494c6fbca209100f0c956a666130c86'
ZIP_MD5 = 'bbf6616928e23ecfef4b717f281c53cc'
WALL = [(127, 127, 127, 255), (255,255,255,255)]
PATH = (0, 255, 0, 255) #green
FILENAME = './ch24_files/mybroken.zip'

def copyPath(path):
  copy = []
  for pix in path:
    copy.append(pix)
  return copy

def isClear(pix):
  return (pix not in WALL)

def checkDirs(maze, startpix):
  # first find the number of available paths
  avail = [False, False, False, False]  # top right bottom left
  availPix = [False, False, False, False]

  if startpix[0] > 0:
    if isClear(maze[startpix[0]-1][startpix[1]]):
      avail[0] = True
      availPix[0] = (startpix[0]-1,startpix[1])
  #check right
  if startpix[1] < 640:
    if isClear(maze[startpix[0]][startpix[1]+1]):
      avail[1] = True
      availPix[1] = (startpix[0],startpix[1]+1)
  #check bottom
  if startpix[0] < 640:
    if isClear(maze[startpix[0]+1][startpix[1]]):
      avail[2] = True
      availPix[2] = (startpix[0]+1,startpix[1])
  #check left
  if startpix[1] > 0:
    if isClear(maze[startpix[0]][startpix[1]-1]):
      avail[3] = True
      availPix[3] = (startpix[0],startpix[1]-1)

  return avail, availPix

# returns true if it can find path to the end from start pix, false otherwise
def isPath(maze, path):

  while True:
    # print len(path)

    startpix = path[-1]

    # break condition
    if startpix[0] == 640:
      return True

    #check dirs
    avail, availPix = checkDirs(maze, startpix)

    if len(path) > 1:
      for i in xrange(4):
        if avail[i]:
          if availPix[i] == path[-2]: #if this pix was just traversed as part of the path
            avail[i] = False
            availPix[i] = False

    if avail.count(True) == 4:
      raise Exception('Invalid State')

    if avail.count(True) == 0:
      # dead end
      return False

    state = itertools.izip(avail, availPix)

    if avail.count(True) == 1:
      # only one path available
      for available, availablePix in state:
        if available:
          path.append(availablePix)

    elif avail.count(True) >= 2:
      break


  # 2 or 3 paths available
  for available, availablePix in state:
    if available:
      path.append(availablePix)
      newPath = copyPath(path)
      if isPath(maze, newPath):
        del path[:]
        path.extend(newPath)
        return True
      else:
        del path[len(path)-1]

  return False


def solveBroken():
  with open(FILENAME, 'rb') as f:
    dat = f.read()

  print len(dat)
  dat = list(dat)
  for i in xrange(len(dat)):
    orig = dat[i]
    print orig
    for j in xrange(256):
      dat[i] = chr(j)
      temp = ''.join(dat)
      if hashlib.md5(temp).hexdigest() == EMAIL_MD5:
        with open(FILENAME, 'wb') as f:
          f.write(temp)
          print 'broke out at index:', i, 'using j:', j
          return
    dat[i] = orig


def solveMaze():
  # sys.setrecursionlimit(50000)

  maze = im.open('maze.png')

  # print maze.mode

  li = list(maze.getdata())

  maze = chunks(li, 641)

  # path = [(0,639)]

  # print isPath(maze, path)
  # print len(path)

  # pickle.dump(path, open('maze-sol.dat', 'wb'))
  path = pickle.load(open('maze-sol.dat', 'rb'))

  # for pix in path:
  #     maze[pix[0]][pix[1]] = PATH
  # new_img = list(itertools.chain(*maze))
  # fim = im.new('RGBA',(641,641))
  # fim.putdata(new_img)
  # fim.show()

  pathdata = []
  for pix in path:
    pathdata.append(maze[pix[0]][pix[1]][0])

  # print len(pathdata)
  # for dat in pathdata[:10:2]:
  #   if dat != (0,0,0,255):
  #     raise Exception('Assumption is wrong!')

  #we can skip every odd element in pathdata
  pathdata = pathdata[1::2]
  dat = ''.join(chr(x) for x in pathdata)
  print dat[:100]
  print len(dat)

  z = ZipFile(StringIO(dat))
  print z.namelist()
  z.extractall(path='./ch24_files/')
  z.close()


if __name__ == '__main__':

  # solveMaze()

  solveBroken()


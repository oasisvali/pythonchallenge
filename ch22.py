from PIL import Image as im
from PIL import ImageDraw
import os
from ch7 import chunks


def extractFrames(inGif, outFolder):
    frame = im.open(inGif)
    nframes = 0
    while frame:
        frame.save( '%s/%s.gif' % (outFolder, nframes ) , 'GIF')
        nframes += 1
        try:
            frame.seek( nframes )
        except EOFError:
            break;
    print 'nframes:', nframes
    return True

if __name__ == '__main__':

  # extractFrames('white.gif', 'ch22_pics')

  imgs = []

  for root, dirs, filenames in os.walk('./ch22_pics/'):
    filenames.remove('.DS_Store')
    for f in sorted(filenames, key=lambda n: int(n.split('.')[0])):
        imgs.append(im.open('./ch22_pics/' + f))


  marks = []

  imgctr = 0
  for img in imgs:
    img = img.convert('RGBA')

    li = list(img.getdata())

    # print '\nCTR:', imgctr, '\n'
    imgctr += 1

    # print img.mode
    # print img.size
    # print len(li)

    li = chunks(li,200)

    # print len(li[0])
    # print len(li)

    rc = 1

    for row in li:
      col = 1
      for pix in row:
        if pix == (8,8,8,255):
          marks.append((rc-1, col-1))

        col += 1
      rc += 1
  
  print len(marks)

  W = 200
  H = 200

  img = im.new("RGB", (W, H), "black")
  draw = ImageDraw.Draw(img)

  cur = ()
  resetctr = 0
  for mark in marks:
    if mark == (100, 100):
      resetctr += 1
      cur = (30*resetctr, 30*resetctr)
      continue
    dx = mark[0] - 100
    dy = mark[1] - 100
    draw.line((cur[0], cur[1], cur[0]+dx, cur[1]+dy), "white")
    cur = (cur[0] + dx, cur[1]+dy)
  img.show()




  

  


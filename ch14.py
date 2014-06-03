from PIL import Image as im

def init_row():
  ret = []
  for i in range(100):
    ret.append([])  # each list holds a pixel
  return ret  

def init():
  ret = []
  for i in range(100):
    ret.append(init_row())    #each list is a row in the final image
  return ret

def split(li):
  ret = []
  for elem in li:
    ret.append([elem])
  return ret

if __name__ == '__main__':

  img = im.open('wire.png')
  print img.mode
  img = list(img.getdata())
  
  fim = init()
  # print fim
  print len(img)

  turn = 0
  pixDone = 0
  secondIterFlag = 0
  ctr = 100
  tRow = 0
  rCol = 99
  lCol = 0
  bRow = 99

  fim[tRow] = split(img[pixDone:pixDone+ctr])
  pixDone += ctr
  turn += 1
  ctr -= 1
  tRow += 1

  while pixDone <= 10000 and ctr > 0:
    # print pixDone
    # print ctr
    if turn == 0: #top
      j = 0
      for i in range(lCol,rCol+1):
        fim[tRow][i].append(img[pixDone:pixDone+ctr][j])
        j+=1
      tRow += 1
    elif turn == 1: #right
      j = 0
      for i in range(tRow,bRow+1):
        fim[i][rCol].append(img[pixDone:pixDone+ctr][j])
        j+=1
      rCol -= 1
    elif turn == 2: #bottom
      j = 0
      for i in reversed(range(lCol,rCol+1)):
        fim[bRow][i].append(img[pixDone:pixDone+ctr][j])
        j+=1
      bRow -= 1
    elif turn == 3: #left
      j = 0
      for i in reversed(range(tRow,bRow+1)):
        fim[i][lCol].append(img[pixDone:pixDone+ctr][j])
        j+=1
      lCol += 1

    pixDone += ctr
    turn += 1
    turn %= 4
    if secondIterFlag == 0:
      secondIterFlag = 1
    elif secondIterFlag == 1:
      ctr -= 1
      secondIterFlag = 0

  complete_img = []
  for row in fim:
    for pix in row:
      complete_img.append(pix[0])

  # print fim
  print len(complete_img)
  
  fim = im.new('RGB',(100,100))
  fim.putdata(complete_img)
  fim.show()


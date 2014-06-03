from PIL import Image as im

if __name__ == '__main__':

  f = open('evil2.gfx', 'rb')

  evil = f.read()
  f.close()

  imgs = [[],[],[],[],[]]

  ctr = 0
  for byte in evil:
    imgs[ctr%5].append(byte)
    ctr += 1

  for i in range(1,6):
    f = open('im' + str(i) + '.jpg', 'wb')
    f.write(''.join(imgs[i-1]))
    f.close()


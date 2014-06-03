from PIL import Image as im
from ch7 import chunks

if __name__ == '__main__':

  # To convert gif to png

  # img = im.open('mozart.gif')
  # new_img = im.new("RGBA", img.size)
  # new_img.paste(img)
  # new_img.save('mozart.png')
  # new_img.show()
 
  img = im.open('mozart.png') 
  print img.mode

  img = list(img.getdata())
  img = chunks(img,640)
  new_img = []

  for row in img:
    
    for i in range(4,len(row)):
      if row[i] == (255, 0, 255, 255) and row[i] == row[i-1] and row[i] == row[i-2] and row[i] == row[i-3] and row[i] == row[i-4]:
        new_img.extend(row[i:] + row[:i])

  # rctr = 0
  # for row in li:
  #   ctr = 0
  #   for pix in row:
  #     if (ctr%2 != 0) and (rctr%2!=0):  #odd if odd row
  #       finlist += [pix]
  #     elif (ctr%2 == 0) and (rctr%2==0):
  #       finlist += [pix]
  #     ctr += 1
  #   rctr+=1
  
  fim = im.new('RGBA',(640,480))
  fim.putdata(new_img)
  fim.show()


from pprint import pprint
import bz2

if __name__ == '__main__':
  with open('silence!.html') as f:
    txt = f.readlines()
  for i, line in enumerate(txt):
    if '</html>' in line:
      break
  txt = txt[i+1:]
  # pprint(txt)

  dat = []
  for line in txt:
    dat.append(line.count(' '))

  datstr = ''.join(chr(x) for x in dat)
  print bz2.decompress(datstr)
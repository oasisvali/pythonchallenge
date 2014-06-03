from difflib import Differ, unified_diff
import gzip
from pprint import pprint

def getVal(lines):
  bytearr = []
  for line in lines:
    bytes = line.split()
    # if len(bytes) == 0:
      # continue
    bytearr += (int(byte, 16) for byte in bytes)
  return bytearray(bytearr)

if __name__ == '__main__':

  f = gzip.open('deltas.gz', 'rb')
  file_content = f.read().splitlines()
  
  f.close()

  info1 = []
  info2 = []

  for line in file_content:
    line1 = line[:54].strip()
    line2 = line[54:].strip()

    # print line1
    # print line2
    # raw_input()

    info1.append(line1)
    info2.append(line2)

  # file1 = '\n'.join(info1)
  # file2 = '\n'.join(info2)

  # f = open('delta1.txt', 'w')
  # f.write(file1)
  # f.close()
  # f = open('delta2.txt', 'w')
  # f.write(file2)
  # f.close()

  differ = Differ()
  result = list(differ.compare(info1,info2))

  common = []
  left = []
  right = []
  neither = []

  for line in result:
    if line[0] == ' ':
      common.append(line[1:])
    elif line[0] == '-':
      left.append(line[1:])
    elif line[0] == '+':
      right.append(line[1:])
    elif line[0] == '?':
      neither.append(line[2:])
    elif line[:2] == '@@':
      continue
    else:
      raise Exception('Problem: %s', line)

  leftVal = getVal(left)
  f = open('left.png', 'wb')
  f.write(leftVal)
  f.close()

  rightVal = getVal(right)
  f = open('right.png', 'wb')
  f.write(rightVal)
  f.close()

  commonVal = getVal(common)
  f = open('common.png', 'wb')
  f.write(commonVal)
  f.close()
def fib(num):
  if num == 1:
    return 1
  elif num == 2:
    return 2
  elif num > 2:
    return (fib(num-1)+fib(num-2))

def nextnum(num):
  num = str(num)
  ctr = 0
  dig = num[0]
  nxt = ''
  for digt in num:
    if digt == dig:
      ctr += 1
      continue
    else:
      nxt += str(ctr)+dig
      dig = digt
      ctr = 1
  nxt += str(ctr)+dig
  return nxt

if __name__ == '__main__':
  res = 1
  for i in range(30):
    # print res
    res = nextnum(res)
  print len(res)

f = open('./input1.txt')
lines = f.readlines()

p = 50
max = 100
result = 0

for l in lines:
  l = l.replace('\n', '')
  dir = l[0:1]
  dif = int(l[1:])
  
  if dir == 'L':
    p -= dif
  elif dir == 'R':
    p += dif

  p = p % max
  if p < 0:
    p = max - p

  if p == 0:
    result += 1

  print(l + '  ' + str(dif) + '  ' + str(p))

print('result: ', result)

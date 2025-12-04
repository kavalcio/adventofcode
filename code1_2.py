f = open('./input1.txt')
lines = f.readlines()

p = 50
max = 100
result = 0

for l in lines:
  # Read instruction
  l = l.replace('\n', '')
  dir = -1 if l[0:1] == 'L' else 1
  dif = int(l[1:])

  # Loop through difference in given direction, count how many times dial passes 0
  for i in range(dif):
    p += dir
    p = p % max
    if p == 0: result += 1

  print(l.ljust(4) + '  dpr:  ' + str(dif * dir).rjust(4)  + '  ' + str(p).rjust(2) , '  ', result)

print('result: ', result)

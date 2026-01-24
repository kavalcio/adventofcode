f = open('./input2.txt')
inputranges = f.read().replace('\n', '').split(',')

result = 0

for inputrange in inputranges:
  [start, end] = inputrange.split('-')

  # Find indices where the first and second halves of the string are identical
  for i in range(int(start), int(end)):
    istr = str(i)
    strlen = len(istr)

    if strlen % 2 != 0: continue

    firsthalf = istr[:strlen // 2]
    secondhalf = istr[strlen // 2:]

    if firsthalf == secondhalf:
      print('found! ', istr)
      result += i

print('result: ', result)


f = open('./input2.txt')
inputranges = f.read().replace('\n', '').split(',')

result = 0

for inputrange in inputranges:
  [start, end] = inputrange.split('-')

  print('--- RANGE: ', start, '  ', end)

  # Find indices that are made up of any repeating substring (i.e. 111, 12312313, 2424, 7373737373)
  for i in range(int(start), int(end)):
    istr = str(i)
    strlen = len(istr)


    for substrlen in range(1, strlen // 2 + 1):
      # String can't be repeating if total length is not a multiple of substr length
      if strlen % substrlen != 0: continue

      # If all substrings match the first substring, we found a repeating string
      is_repeating = True
      for k in range(1, strlen // substrlen):
        if istr[:substrlen] != istr[k*substrlen:(k+1)*substrlen]:
          is_repeating = False
          break
      
      if is_repeating:
        print('found! ', istr)
        result += i
        # If one repeating substr is found for the current index, break loop so we don't count it multiple times
        break

print('result: ', result)


f = open('./input3.txt')
lines = f.readlines()

num_digits = 12
digits = []
digit_indices = []
result = 0

for index, line in enumerate(lines):
  line = line.replace('\n', '')
  digits.clear()
  digit_indices.clear()
  for i in range(num_digits):
    digits.append(0)
    digit_indices.append(-1)

  # For each digit, find the largest digit that would leave enough room for the remaining digits to be picked
  for i in range(num_digits):
    
    start_index = digit_indices[max(i-1, 0)] + 1
    end_index = len(line) - (num_digits - i - 1)
    
    for j in range(start_index, end_index):
      num = int(line[j:j+1])
      if num > digits[i]:
        digits[i] = num
        digit_indices[i] = j

    # print(str(index), 'line: ', line, 'start_i:',start_index,'end_i:',end_index, ' i: ', i, ' dx: ', '.'.join(map(str, digits)), ' ix: ', '.'.join(map(str, digit_indices)))

  total = int(''.join(map(str, digits)))
  result += total

  print('>> line: ', line, ' digits: ', str(total))
    
print('result: ', result)

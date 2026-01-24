f = open('./input3.txt')
lines = f.readlines()

result = 0

for line in lines:
  line = line.replace('\n', '')
  first_digit = 0
  second_digit = 0
  first_digit_index = -1
  second_digit_index = -1

  # First digit will be largest integer that's not at the end of the string
  # If repeating, pick the earlier index (to give more options for the second digit)
  for i in range(len(line) - 1):
    num = int(line[i:i+1])
    if num > first_digit:
      first_digit = num
      first_digit_index = i

  # Second digit will the the largest integer that comes after the first digit's index
  for j in range(first_digit_index + 1, len(line)):
    num = int(line[j:j+1])
    if num > second_digit:
      second_digit = num
      second_digit_index = j

  total = int(str(first_digit) + str(second_digit))
  result += total

  print('line: ', line, ' number: ', first_digit, second_digit, ' index: ', first_digit_index, ',', second_digit_index)

print('result: ', result)


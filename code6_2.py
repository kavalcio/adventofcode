from functools import reduce

f = open('./input6.txt')
lines = f.readlines()

result = 0

cells = []

def is_not_empty(item):
  return item != ''

def perform_op(op, a, b):
  if (op == '*'):
    return a * b
  else:
    return a + b
  
def find_first_nonempty_char(chars):
  match = None
  for index, char in enumerate(chars):
    if char != ' ':
      match = index
      break
  return match
  

row_count = len(lines)

for i in range(len(lines)):
  lines[i] = lines[i].replace('\n', ' \n')
  lines[i] = list(lines[i])


reached_end_of_file = False
i = 0

while not reached_end_of_file:
  # Grab char on the operations line
  op_char = lines[row_count - 1][i]

  # Find index of next operation char, which will give us the column range of numbers that are part of this operation
  condition = lambda x: x != ' '
  next_op_index = find_first_nonempty_char(lines[row_count - 1][i + 1 :]) + i + 1
  next_op_char = lines[row_count - 1][next_op_index]

  # Parse numbers vertically into an array
  parsed_nums = []
  for j in range(next_op_index - 1 - i):
    num_str = ''
    for k in range(row_count - 1):
      num_char = lines[k][j + i]
      if num_char == ' ': continue
      num_str = num_str + num_char
    parsed_nums.append(int(num_str))

  # Perform operation on parsed numbers, add to total result
  res = reduce(lambda x, y: perform_op(op_char, x, y), parsed_nums)
  result += res

  print('op:', op_char, parsed_nums, res)

  # Break loop when end of line is reached
  if (next_op_char == '\n'):
    reached_end_of_file = True

  i = next_op_index

print('result: ', result)


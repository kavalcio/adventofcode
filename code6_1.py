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
    

# Build nested array
for l in lines:
  l = l.replace('\n', '')
  cells.append(list(filter(is_not_empty, l.split(' '))))

for i in range(len(cells[0])):
  operation = cells[len(cells) - 1][i]
  nums = []
  for j in range(len(cells) - 1):
    nums.append(int(cells[j][i]))
  res = reduce(lambda x, y: perform_op(operation, x, y), nums)
  result += res
  print('op', operation, nums, res)

print('result: ', result)

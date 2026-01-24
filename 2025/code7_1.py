f = open('./input7.txt')
lines = f.readlines()

for i in range(len(lines)):
  lines[i] = list(lines[i].replace('\n', '').replace('S', '|'))

row_count = len(lines)
col_count = len(lines[0])

times_split = 0

# Loop through rows and cells in order (skip last row, as there can be no more splits)
for row in range(row_count - 1):
  for col in range(col_count):
    # If cell has a ray, propagate it below
    if lines[row][col] == '|':
      # If next cell is empty space, ray travels uninhibited
      if lines[row + 1][col] == '.':
        lines[row + 1][col] = '|'
      # If next cell is a splitter, ray splits in two
      if lines[row + 1][col] == '^':
        lines[row + 1][col - 1] = '|'
        lines[row + 1][col + 1] = '|'
        times_split += 1

print('result: ', times_split)

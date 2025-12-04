f = open('./input4.txt')
lines = f.readlines()

result = 0
max_height = 138
max_width = 138
max_neighbours = 3

cells = []

print('max_height', max_height, 'max_width', max_width)

# Build nested array
for l in lines:
  l = l.replace('\n', '')
  cells.append(list(l))

def parse_cells():
  moved_cells = 0

  # Loop through rows
  for i in range(len(lines)):
    # Loop through columns
    for j in range(max_width):
      # Skip if cell has no paper
      if cells[i][j] == '.': continue

      # For each elements, check the 8 adjacent cells for # of neightbours
      neighbours = 0
      for y in range(i - 1, i + 2):
        # Check for index out of bound
        if y < 0 or y > max_height - 1: continue
        for x in range(j - 1, j + 2):
          # Check for index out of bound
          if x < 0 or x > max_width - 1: continue
          # Skip the center cell
          if y == i and x == j: continue

          cell = cells[y][x]
          if cell == '@': neighbours += 1

      # If cell is in an accessible position, move it
      if neighbours <= max_neighbours:
        cells[i][j] = '.'
        moved_cells += 1

  return moved_cells

# Parse through list and remove cells as we go until no cells can be moved
loop_count = 0
while True:
  print('loop', loop_count)
  mc = parse_cells()
  if mc == 0: break
  result += mc
  loop_count += 1


print('result: ', result)

f = open('./input9.txt')
lines = f.readlines()

for i in range(len(lines)):
  lines[i] = lines[i].replace('\n', '').split(',')
  for j in range(len(lines[i])):
    lines[i][j] = int(lines[i][j])

area = 0

edges = []
# TODO: create list of edges of the valid area
for i in range(len(lines) - 1):
  edges.append({ 'x1': lines[i][0], 'x2': lines[i+1][0], 'y1': lines[i][1], 'y2': lines[i+1][1] })


def check_intersection(line1, line2):
  

for i in range(len(lines)):
  for j in range(i + 1, len(lines)):
    new_area = (abs(lines[i][0] - lines[j][0]) + 1) * (abs(lines[i][1] - lines[j][1]) + 1)
    if new_area > area:
      # TODO: parse through the list of edges, check whether the 4 edges of this rectangle collide with any of them
      # If any edge has an orthogonal collision (not at the tips), no match
      # If no edges have orthogonal collisions, check a random point in the middle. But how do i check that?
      print('MAX:', i, j, lines[i], lines[j], new_area)
      area = new_area

print('result:', edges)

# 4758460754 too low

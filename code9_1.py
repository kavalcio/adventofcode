f = open('./input9.txt')
lines = f.readlines()

for i in range(len(lines)):
  lines[i] = lines[i].replace('\n', '').split(',')
  for j in range(len(lines[i])):
    lines[i][j] = int(lines[i][j])

area = 0

for i in range(len(lines)):
  for j in range(i + 1, len(lines)):
    new_area = (abs(lines[i][0] - lines[j][0]) + 1) * (abs(lines[i][1] - lines[j][1]) + 1)
    if new_area > area:
      print('MAX:', i, j, lines[i], lines[j], new_area)
      area = new_area

print('result:', area)

# 4758460754 too low

import math

f = open('./input8.txt')
lines = f.readlines()

for i in range(len(lines)):
  lines[i] = lines[i].replace('\n', '').split(',')
  for j in range(len(lines[i])):
    lines[i][j] = int(lines[i][j])

result = 0

distances = []

def find_dist(point1, point2):
  return math.sqrt(pow(point1[0] - point2[0], 2) + pow(point1[1] - point2[1], 2) + pow(point1[2] - point2[2], 2))


def is_not_empty(item):
  return item != None


for i in range(len(lines)):
  for j in range(i + 1, len(lines)):
    dist = find_dist(lines[i], lines[j])
    distances.append({ 'i': i, 'j': j, 'dist': dist, 'c1': lines[i], 'c2': lines[j] })


distances.sort(key=lambda item: item['dist'])

groups = []
point_to_group_id = {}

for k, items in enumerate(distances):
  i = items['i']
  j = items['j']
  group1 = point_to_group_id.get(i)
  group2 = point_to_group_id.get(j)

  if group1 == None and group2 == None:
    groups.append([i, j])
    point_to_group_id[i] = len(groups) - 1
    point_to_group_id[j] = len(groups) - 1
    print('N: ', point_to_group_id[i], i, j)
  elif group1 != None and group2 != None and group1 != group2:
    merged_group = list(set(groups[group1] + groups[group2]))
    groups[group1] = None
    groups[group2] = None
    groups.append(merged_group)
    for x in merged_group:
      point_to_group_id[x] = len(groups) - 1
    point_to_group_id[i] = len(groups) - 1
    point_to_group_id[j] = len(groups) - 1
    print('Merge: ', point_to_group_id[i], i, j)
  elif group1 != None and group2 == None:
    print('i: ', group1, i, j)
    groups[group1].append(j)
    point_to_group_id[j] = group1
  elif group2 != None and group1 == None:
    print('J: ', group2, i, j)
    groups[group2].append(i)
    point_to_group_id[i] = group2


  # Stop parsing list when every item has been added to a circuit, and we've first merged all circuits into one
  le = len(list(filter(is_not_empty, groups)))
  if k > 10 and le > 0 and le < 2 and len(point_to_group_id) == len(lines):
    print('break', k, items)
    print('result: ', items['c1'][0] * items['c2'][0])
    break


groups = list(filter(is_not_empty, groups))
groups.sort(key=lambda item: len(item), reverse=True)

# print('result: ', result)

# 520594911 too high


# Write distance order to output file
for i, d in enumerate(groups):
  groups[i] = str(d)
outstr = '\n'.join(groups)
with open('output8.txt', 'w') as o:
  o.write(outstr)

for i, d in enumerate(distances):
  distances[i] = str(d)
outstr = '\n'.join(distances)
with open('distances.txt', 'w') as o:
  o.write(outstr)

import shapely

f = open("./input9.txt")
lines = f.readlines()

for i in range(len(lines)):
  lines[i] = lines[i].replace("\n", "").split(",")
  for j in range(len(lines[i])):
    lines[i][j] = int(lines[i][j])

area = 0

vertices = []
for i in range(len(lines)):
  row = (float(lines[i][0]), float(lines[i][1]))
  vertices.append(row)

polygon_full = shapely.Polygon(vertices)

for i in range(len(lines)):
  vertex_i = lines[i]
  for j in range(i + 1, len(lines)):
    vertex_j = lines[j]

    new_area = (abs(vertex_i[0] - vertex_j[0]) + 1) * (abs(vertex_i[1] - vertex_j[1]) + 1)
    if new_area <= area: continue

    polygon_partial = shapely.Polygon([(vertex_i[0],vertex_j[1]), (vertex_j[0], vertex_j[1]), (vertex_j[0],vertex_i[1]), (vertex_i[0],vertex_i[1]) ])
    if shapely.within(polygon_partial,polygon_full):
      print("-->> MAX:", i, j, lines[i], lines[j], new_area)
      area = new_area

print("result:", area)

# 3062848107 too high
# 3036655402 too high
# 2973394524 too high

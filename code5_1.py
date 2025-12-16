f = open('./input5.txt')
lines = f.readlines()

splitIndex = lines.index('\n')

fresh_id_ranges = lines[:splitIndex]
available_ids = lines[splitIndex + 1:]

parsed_fresh_id_ranges = []
for i in range(len(fresh_id_ranges)):
  [start, end] = fresh_id_ranges[i].replace('\n', '').split('-')
  parsed_fresh_id_ranges.append([int(start), int(end)])

result = 0

for available_id in available_ids:
  available_id = int(available_id.replace('\n', ''))
  for [start, end] in parsed_fresh_id_ranges:
    if available_id >= start and available_id <= end:
      result += 1
      break

print('result', result)

# 3185 too high
# 982 too high

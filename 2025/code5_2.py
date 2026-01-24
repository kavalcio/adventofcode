f = open('./input5.txt')
lines = f.readlines()

splitIndex = lines.index('\n')

id_ranges = lines[:splitIndex]

parsed_id_ranges = []
for i in range(len(id_ranges)):
  [start, end] = id_ranges[i].replace('\n', '').split('-')
  parsed_id_ranges.append([int(start), int(end)])

result = 0

final_id_ranges = []

# Go through each id range in the input
for parsed_id_range in parsed_id_ranges:
  [start_1, end_1] = parsed_id_range

  # Check if there are any overlaps with ranges in the final list
  for index, [start_2, end_2] in enumerate(final_id_ranges):
    # If overlap found, update value and pop old range
    if not (start_1 > end_2 or end_1 < start_2):
      print('overlap', start_1, end_1, '-', start_2, end_2, '-', min(start_1, start_2), max(end_1, end_2))
      final_id_ranges.pop(index)
      start_1 = min(start_1, start_2)
      end_1 = max(end_1, end_2)

  final_id_ranges.append([start_1, end_1])


# Go through final id ranges, add up total range
for index, [start_1, end_1] in enumerate(final_id_ranges):
  result += end_1 - start_1 + 1

print('result', result)

# 558879225281492 too high
# 373466207517565 too high
# 384410904181775
# 407907035255119
# 418808296269206
# 369761800782619

from functools import cache

f = open('./input7.txt')
grid = f.readlines()

for i in range(len(grid)):
  grid[i] = list(grid[i].replace('\n', ''))

row_count = len(grid)
col_count = len(grid[0])

timelines = 1

# This caches the function result, so that paths that get traversed multiple times aren't recalculated every time
@cache
def shoot_ray(row_start, col_start):
  new_timelines = 0
  if row_start == row_count - 1:
    return 0
  if grid[row_start + 1][col_start] == '^':
    # Every time ray hits a splitter, a new timeline is created
    new_timelines += 1
    # After a split, recursively shoot ray in both new timelines
    new_timelines_left = shoot_ray(row_start + 1, col_start - 1)
    new_timelines_right = shoot_ray(row_start + 1, col_start + 1)
    # Add the timeline count of these 2 new paths to the total
    new_timelines += new_timelines_left + new_timelines_right
  else:
    # If no splitter is hit, just propagate the ray downward
    new_timelines += shoot_ray(row_start + 1, col_start)
  return new_timelines

row_initial = 0
col_initial = grid[0].index('S')

timelines += shoot_ray(row_initial, col_initial)

print('result: ', timelines)

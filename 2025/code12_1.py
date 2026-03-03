
import math
from functools import cache

def check_toys_can_fit(space_width, space_height, toy_counts, toy_sizes):
  # Assume all toys take 3x3 space, check if toys fit into the number of 3x3 slots. If they do return true early
  total_toy_count = sum(toy_counts)
  total_toy_slot_count = math.floor(space_width/3) * math.floor(space_height/3)
  if (total_toy_slot_count >= total_toy_count):
    return True
  
  # Add up total cell counts toys take up. If it's higher than total cell count in space, return false early
  total_cells_needed = sum([count * size for count, size in zip(toy_counts, toy_sizes)])
  total_cells_available = space_height * space_width
  if (total_cells_needed > total_cells_available):
    return False
  
  # TODO: attempt to incrementally and recursively add all toys to the space until we either find a success case or we exhaust all options
  # Note: no need in the end, the shortcuts were enough
  return 'maybe'
  

# # This is a cached function that takes:
# # - slot_state: 3x3 board space that this attempt is being made in.
# # - toy_state: 3x3 shape of the toy to add into the slot. Rotation and flipping already applied.
# # There are only so many 3x3 slot states and 3x3 toy shapes possible. After a few iterations this will start returning cached values only
# # @cache
# def attempt_insert_trimmed(slot_state, toy_state):
#   return False

# # 258
# # 1674
# # 40*6 + 46*5 + 38*7 + 44*7 + 44*7 + 46*7
# def attempt_insert(board_state, toy_id, orientation, is_flipped):
#   return False


f = open('./input12.txt')
lines = f.readlines()

toy_shapes = []
toy_sizes = []
for i in range(6):
  shape = []
  shape.extend(list(lines[i * 5 + 1].replace('\n', '')))
  shape.extend(list(lines[i * 5 + 2].replace('\n', '')))
  shape.extend(list(lines[i * 5 + 3].replace('\n', '')))
  toy_shapes.append(shape)
  toy_size = 0
  for k, n in enumerate(shape):
    if n == '#': toy_size += 1
  toy_sizes.append(toy_size)

inputs = []
for i in range(30, 1030):
  width = int(lines[i].split('x')[0])
  height = int(lines[i].split('x')[1].split(':')[0])
  toy_counts = [int(x) for x in lines[i].replace('\n', '').split(': ')[1].split(' ')]

  input = { 'width': width, 'height': height, 'toy_counts': toy_counts }
  inputs.append(input)

num_solvable = 0
num_calcs_needed = 0
for index in range(len(inputs)):
# for index in range(5):
  input = inputs[index]
  res = check_toys_can_fit(input['width'], input['height'], input['toy_counts'], toy_sizes)
  print(index, res)
  if res == 'maybe':
    num_calcs_needed += 1
  elif res == True:
    num_solvable += 1

print('result', num_solvable)

# Funny, you can actually solve this entire part by using the two shortcuts i did
# 451

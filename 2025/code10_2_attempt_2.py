# Attempt at solution using system of linear equations, can't deal with free variables

# https://www.reddit.com/r/adventofcode/comments/1pity70/comment/nt8ve95/?utm_source=share&utm_medium=web3x&utm_name=web3xcss&utm_term=1&utm_content=share_button

import sympy as sp

f = open('./input10.txt')
lines = f.readlines()

buttons_list = []
joltage_list = []

# Parse input into list of target jotage configurations and buttons
for i in range(len(lines)):
  sections = lines[i].replace("\n", "").split(" ")
  buttons = [b[1:-1].split(',') for b in sections[1:-1]]
  buttons = [[int(x) for x in lst] for lst in buttons]
  joltages = [int(x) for x in sections[-1][1:-1].split(',')]
  buttons_list.append(buttons)
  joltage_list.append(joltages)


# m = sp.Matrix([[1,0,1,1,0,32],
#            [0,1,0,0,1,23],
#            [1,1,0,1,0,39],
#            [1,0,0,0,1,9]])

# m = sp.Matrix([[1,0,1,0,19],
#            [0,0,1,1,10],
#            [1,1,1,0,26],
#            [0,1,0,0,7]])

def check_solution(values, matrix):
  height = matrix.shape[0]
  width = matrix.shape[1]

  for y in range(height):
    target = matrix[y, width - 1]
    m_row = matrix.row(y).tolist()[0]
    value_sum = sum([v * m_row[i] for i, v in enumerate(values)])
    if target != value_sum:
      return False
  return True

def calculate_press_count(buttons, joltages, n, detailed_logs):
  rows = []
  for ji, j in enumerate(joltages):
    row = []
    for b in buttons:
      if ji in b:
        row.append(1)
      else:
        row.append(0)
    row.append(j)
    rows.append(row)

  m = sp.Matrix(rows)

  m_rref, pivots = m.rref() # Compute reduced row echelon form (rref)
  free_variables =  [i for i in range(len(buttons)) if i not in pivots]
  if detailed_logs:
    print('free_variables', free_variables)
    print('pivots', pivots)
    sp.pprint(m_rref)


  # press_list = [m_rref[p, m_rref.shape[1] - 1] for p in pivots]
  press_list = []
  for p in pivots:
    # Find row that has the pivot, extract the press count from it
    col = [x[0] for x in m_rref.col(p).tolist()]
    # print('col', col)
    pivot_row_index = col.index(1)
    press_count = m_rref[pivot_row_index, m_rref.shape[1] - 1]
    press_list.append(press_count)

  sol = check_solution([23,15,6,10,20,4,0,0,13], m_rref)
  print('sol', sol)

  total = sum(press_list)
  print('Line', n+1, '-', total)
  return total

# result = 0
# for n in range(len(lines)):
#   presses = calculate_press_count(buttons_list[n], joltage_list[n], n, False)
#   result += presses
# print('result', result)

calculate_press_count(buttons_list[1], joltage_list[1], 1, True)

# 17908 too high

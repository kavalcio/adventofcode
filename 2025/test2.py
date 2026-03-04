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
  # Build matrix to solve system of equations
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

  # Compute the matrix's reduced row echelon form (rref) and get pivots, free variables
  m_rref, pivots = m.rref()
  free_variables =  [i for i in range(len(buttons)) if i not in pivots]
  if detailed_logs:
    print('free_variables', free_variables)
    print('pivots', pivots)
    sp.pprint(m_rref)

  # Free variables can be whatever value, with some limitations:
  # - They still have to satisfy each equation in a way that keeps all the other variables at 0 or above. You can't have negative presses.
  # - A free variable's coefficients across the system have to add up to a positive value - otherwise a non-zero value would increase the total number of presses.
  # - In fact, the coefficients have to add up to at least 2 - if it's 1, each press saved is equally offset by the extra press of the free variable
  # - If there are multiple free variables with coefficients that add up the >= 2, then we need to check every combination of valid values between all of them
  # - We should pick the values that minimize the sum of clicks for each button

  # TODO: Example values, replace with calculation to get real values
  free_variable_values = {
    6: 3,
    7: 0
  }

  press_list = [] # Number of times each button in the list is pressed
  for i, p in enumerate(pivots):
    # Press count is the final number in the row, minus the difference caused by any free variables
    # Don't forget to check press_count is above zero. If not, break.
    press_count = m_rref[i, m_rref.shape[1] - 1]
    pivot_col_index = m_rref.row(i).tolist()[0].index(1)

    # Loop through free variables
    for j in range(pivot_col_index + 1, m_rref.shape[1] - 1):
      free_var_coeff = m_rref[i, j]
      free_var_value = free_variable_values.get(j)

      # If free variable is 0, no need to do anything else
      if free_var_value == None:
        continue
      diff = free_var_coeff * free_var_value

      # Add up the difference caused by the value of the free variable
      press_count -= diff
      # print('col', i, j, free_var_coeff, free_var_value, 'diff', diff, press_count)

    press_list.append(press_count)

  # Add the number of presses of the free variable itself
  for f in list(free_variable_values.values()):
    press_list.append(f)

  # Based on number of free variables, generate list of possible solutions
  # possible_solutions = []
  # if len(free_variables) == 0:
  #   possible_solutions.append([x[0] for x in m_rref.col(m_rref.shape[1] - 1).tolist()])
  # else:



  # TODO: Brute force parse through solutions and find once with smallest button press count

  sol = check_solution([23,15,6,10,20,4,0,0,13], m_rref)
  print('sol', sol)

  total = sum(press_list)
  # print('Line', n+1, '-', total)
  return total

# Go through list of inputs, calculate press count for each input and add up results
# result = 0
# for n in range(len(lines)):
#   presses = calculate_press_count(buttons_list[n], joltage_list[n], n, False)
#   result += presses
# print('result', result)

# Test individual line
calculate_press_count(buttons_list[1], joltage_list[1], 1, True)

# 17908 too high

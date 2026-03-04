# https://www.reddit.com/r/adventofcode/comments/1pity70/comment/nt8ve95/?utm_source=share&utm_medium=web3x&utm_name=web3xcss&utm_term=1&utm_content=share_button

import sympy as sp
import copy

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

# Given a dict of values for each free variable, an array of pivot indexes, and the solution matrix:
# - Compute the values of each variable. If any are below 0, return false (no solution)
# - Otherwise return the total press count which is the sum of all variables, including the free variables
def test_solution(free_variable_values, pivots, m_rref):
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

    if press_count < 0:
      print('Too far', i, p)
      return False
    press_list.append(press_count)

  # Add the number of presses of the free variable itself
  for f in list(free_variable_values.values()):
    press_list.append(f)

  # Based on number of free variables, generate list of possible solutions
  # possible_solutions = []
  # if len(free_variables) == 0:
  #   possible_solutions.append([x[0] for x in m_rref.col(m_rref.shape[1] - 1).tolist()])
  # else:

  total = sum(press_list)
  return total

# Build a system of equations for an input row to find its possible solutions.
# For each possible solution, plug values into test_solution.
# Test every valid solution, then return the smallest total press count computed.
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

  # Find free variables that have a coefficient sum >= 2
  # Create a dict where each starts at 0. Plug the values into test_solution and get a sum value in return
  # Keep track of the lowest result returned. Keep incrementing values in the dict until test_solution returns False
  # Return the lowest result.

  potential_free_variable_solutions = []
  parsed_solutions = []

  free_variables_to_parse_through = []
  for v in free_variables:
    coefficient_sum = sum([x[0] for x in m_rref.col(v).tolist()])
    if coefficient_sum >= 2:
      free_variables_to_parse_through.append(v)
  # print('free_variables_to_parse_through', free_variables_to_parse_through)

  # Start with initial solution where all free variables = 0
  sol = {}
  for v in free_variables_to_parse_through:
    sol[v] = 0
  potential_free_variable_solutions.append(sol)

  min_presses = 1000000000
  while len(potential_free_variable_solutions) > 0:
    # Pop first solution off the top of the queue, add it to parsed solutions
    sol = potential_free_variable_solutions.pop(0)
    parsed_solutions.append(sol)
    print('sol', sol)

    result = test_solution(sol, pivots, m_rref)

    # If solution is invalid, this is a dead end. Continue parsing through other existing solutions
    if result == False:
      continue

    # If solution is valid, continue exploring this path by pushing more possible solutions onto the queue (if it hasn't been parsed yet)
    for v in free_variables_to_parse_through:
      newsol = copy.deepcopy(sol)
      newsol[v] += 1
      if any(s == newsol for s in parsed_solutions) or any(s == newsol for s in potential_free_variable_solutions):
        continue
      potential_free_variable_solutions.append(newsol)

    # If new solution is better than the current best, save it
    if result < min_presses:
      print('>>> new best solution', result)
      min_presses = result

  # min_presses = 1000000000
  # for s in potential_free_variable_solutions:
  #   result = test_solution(s, pivots, m_rref)
  #   if result == False:
  #     continue
  #   if result < min_presses:
  #     print('new best solution', result)
  #     min_presses = result

  # total_presses = test_solution(free_variable_values, pivots, m_rref) 
  print('Line', n+1, '->', min_presses)
  return min_presses




# Go through list of inputs, calculate press count for each input and add up results
# result = 0
# for n in range(len(lines)):
#   presses = calculate_press_count(buttons_list[n], joltage_list[n], n, False)
#   result += presses
# print('result', result)

# Test individual line
# calculate_press_count(buttons_list[1], joltage_list[1], 1, True)
calculate_press_count(buttons_list[9], joltage_list[9], 9, True)

# 17908 too high

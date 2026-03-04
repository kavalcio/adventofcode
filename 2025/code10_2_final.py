# Final attempt, uses z3 to solve system of equations. Works!

from z3 import *

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

# Creates a system of linear equations with relevant constraints and uses z3 to find the optimized solution
def solve_input(joltages, buttons):
  equations = []
  var_count = len(buttons)
  vars = []
  for i in range(var_count):
    vars.append(Int('v%d' % i))

  # Build equations that make up the system
  for ji, j in enumerate(joltages):
    vars_in_equation = []
    for bi, b in enumerate(buttons):
      if ji in b:
        vars_in_equation.append(vars[bi])
    equations.append(sum(vars_in_equation) == j)

  for v in vars:
    equations.append(v >= 0)

  # Define constraints for the optimization problem
  o = Optimize()
  o.add(equations)
  o.minimize(sum(vars))

  # Solve and print values
  m = o.model()
  values_list = [m[d].as_long() for d in m]
  solution = sum(values_list)

  return solution

# Run solver for all inputs, sum total presses
total = 0
for li in range(len(lines)):
  solution = solve_input(joltage_list[li], buttons_list[li])
  total += solution
  print('res', li, solution)

print('total', total)

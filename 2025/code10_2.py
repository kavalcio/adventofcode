import numpy
import itertools

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

# print('buttons_list', buttons_list)
# print('joltage_list', joltage_list)

total_presses = 0

def check_match(joltages_target, buttons, button_presses):
  joltages_current = [0 for i in joltages_target]
  # Loop through each button
  for b in range(len(buttons)):
    press_count = button_presses[b]
    if press_count == 0: continue
    # Loop through the times the button is pressed
    for i in range(press_count):
      affected_joltages = buttons[b]
      # Loop through the joltages that the button affects, and increment them
      for j in affected_joltages:
        joltages_current[j] += 1
  # Check if current jotalge configuration matches target
  return joltages_current == joltages_target

def generate_button_press_sequences(button_count, press_count):
  masks = numpy.identity(button_count, dtype=int)
  for c in itertools.combinations_with_replacement(masks, press_count): 
    yield sum(c)

for i in range(len(lines)):
  # For each device, find the lowest number of button presses that satisfies the requirement
  joltages = joltage_list[i]
  presses = max(joltages)
  while True:
    match_found = False
    buttons = buttons_list[i]

    # For current presses count, try every combination of button presses and check for a match
    sequences = numpy.array(list(generate_button_press_sequences(len(buttons), presses)))
    for s, sequence in enumerate(sequences):
      print('i', i, presses, sequence)
      match_found = check_match(joltages, buttons, sequence)
      if match_found: break

    if match_found:
      print('>>> matchfound', i, presses)
      break
    
    # If match not found, increment button press count and try again
    presses += 1

  # When match is found, add button press count to total presses
  total_presses += presses

print('result', total_presses)

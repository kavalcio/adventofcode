import numpy
import itertools

f = open('./input10.txt')
lines = f.readlines()

lights_list = []
buttons_list = []

# Parse input into list of target light configurations and buttons
for i in range(len(lines)):
  sections = lines[i].replace("\n", "").split(" ")
  lights = list(sections[0][1:-1])
  buttons = [b[1:-1].split(',') for b in sections[1:-1]]
  buttons = [[int(x) for x in lst] for lst in buttons]
  lights_list.append(lights)
  buttons_list.append(buttons)

total_presses = 0

def check_match(lights_target, buttons, button_presses):
  lights_current = ['.' for i in lights_target]
  # Loop through each button
  for b in range(len(buttons)):
    press_count = button_presses[b]
    if press_count == 0: continue
    # Loop through the times the button is pressed
    for i in range(press_count):
      affected_lights = buttons[b]
      # Loop through the lights that the button affects, and flip them
      for l in affected_lights:
        if lights_current[l] == '.':
          lights_current[l] = '#'
        else:
          lights_current[l] = '.'
  # Check if current light configuration matches target
  return lights_current == lights_target

def generate_button_press_sequences(button_count, press_count):
  masks = numpy.identity(button_count, dtype=int)
  for c in itertools.combinations_with_replacement(masks, press_count): 
    yield sum(c)

for i in range(len(lines)):
  # For each device, find the lowest number of button presses that satisfies the requirement
  presses = 1
  while True:
    match_found = False
    buttons = buttons_list[i]

    # For current presses count, try every combination of button presses and check for a match
    sequences = numpy.array(list(generate_button_press_sequences(len(buttons), presses)))
    for s, sequence in enumerate(sequences):
      match_found = check_match(lights_list[i], buttons, sequence)
      if match_found: break

    if match_found:
      print('matchfound', i, presses)
      break
    
    # If match not found, increment button press count and try again
    presses += 1

  # When match is found, add button press count to total presses
  total_presses += presses

print('result', total_presses)

# 457
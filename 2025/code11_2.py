from functools import cache

f = open('./input11.txt')
lines = f.readlines()

devices = {}

for i in range(len(lines)):
  lines[i] = lines[i].replace('\n', '').split(' ')
  devices[lines[i][0][:-1]] = lines[i][1:]
  
# print('devices: ', devices)

@cache
def find_paths_to_out(start_device, is_fft_found, is_dac_found):
  paths = devices[start_device]
  new_routes_found = 0
  for p in paths:
    if p == 'out':
      if is_fft_found and is_dac_found:
        new_routes_found += 1
    else:
      new_routes_found += find_paths_to_out(p, is_fft_found or p == 'fft', is_dac_found or p == 'dac')
  print('resolving', start_device, new_routes_found)
  return new_routes_found

result = find_paths_to_out('svr', False, False)

print('result: ', result)

# 525518050323600
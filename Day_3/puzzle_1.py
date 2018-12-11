import numpy, re, time

PUZZLE_INPUT = 'day_3_input.txt'
SIDE_LENGTH = 1000

def get_puzzle_input(puzzle_file):
  with open(puzzle_file) as file_input:
    claims = [line.rstrip('\n') for line in file_input]
  return map(lambda claim: map(int, re.findall(r'\d+', claim)), claims)

def get_initial_fabric(side_length):
  return numpy.zeros((side_length, side_length))

def claimize_fabric(claims, fabric):
  for id, x, y, width, height in claims:
    fabric[x : x + width, y : y + height] += 1

def determine_overlaps(fabric):
  return len(numpy.where(fabric > 1)[0])

t = time.process_time()
fabric = get_initial_fabric(SIDE_LENGTH)
claims = get_puzzle_input(PUZZLE_INPUT)
claimize_fabric(claims, fabric)
overlaps = determine_overlaps(fabric)
elapsed = round(time.process_time() - t, 4)

print(f'overlapping square inches of fabric: {overlaps}')
print(f'in {elapsed} seconds')

import numpy, re, time

PUZZLE_INPUT = 'day_3_input.txt'
SIDE_LENGTH = 1000

def gen_claims(claim_file):
  with open(claim_file) as file_input:
    claims = [line.rstrip('\n') for line in file_input]
  return map(lambda claim: map(int, re.findall(r'\d+', claim)), claims)

def get_initial_fabric(side_length):
  return numpy.zeros((side_length, side_length))

def claimize_fabric(fabric):
  for id, x, y, width, height in gen_claims(PUZZLE_INPUT):
    fabric[x : x + width, y : y + height] += 1

def find_non_overlapping_claim(claimized_fabric):
  for id, x, y, width, height in gen_claims(PUZZLE_INPUT):
    if numpy.all(claimized_fabric[x : x + width, y : y + height] == 1):
      return id

t = time.process_time()
fabric = get_initial_fabric(SIDE_LENGTH)
claimize_fabric(fabric)
target_id = find_non_overlapping_claim(fabric)
elapsed = round(time.process_time() - t, 4)

print(f'non-overlapping claim ID: {target_id}')
print(f'in {elapsed} seconds')

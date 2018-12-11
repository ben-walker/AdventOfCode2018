import time
from collections import Counter

PUZZLE_INPUT = 'day_2_input.txt'

def get_puzzle_input(puzzle_file):
  with open(puzzle_file) as file_input:
    return [line.rstrip('\n') for line in file_input]

def compute_checksum(box_ids):
  twos_count = 0
  threes_count = 0
  for id in box_ids:
    common_counts = Counter(id).values()
    if 2 in common_counts: twos_count += 1
    if 3 in common_counts: threes_count += 1
  return twos_count * threes_count

t = time.process_time()
box_ids = get_puzzle_input(PUZZLE_INPUT)
checksum = compute_checksum(box_ids)
elapsed = round(time.process_time() - t, 4)

print(f'checksum for box IDs: {checksum}')
print(f'in {elapsed} seconds')

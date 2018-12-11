import itertools, time

PUZZLE_INPUT = 'day_1_input.txt'

def get_puzzle_input(puzzle_file):
  with open(puzzle_file) as file_input:
    return [int(line.rstrip('\n')) for line in file_input]

def find_first_duplicate(changes):
  freq = 0
  found = set()
  for change in itertools.cycle(changes):
    freq += change
    if freq in found:
      return freq
    found.add(freq)

t = time.process_time()
changes = get_puzzle_input(PUZZLE_INPUT)
first_duplicate = find_first_duplicate(changes)
elapsed = round(time.process_time() - t, 4)

print(f'first duplicate frequency: {first_duplicate}')
print(f'in {elapsed} seconds')

import time

PUZZLE_INPUT = 'day_1_input.txt'

def get_puzzle_input(puzzle_file):
  with open(puzzle_file) as file_input:
    return [int(line.rstrip('\n')) for line in file_input]

def calculate_frequency(changes):
  return sum(changes)

t = time.process_time()
changes = get_puzzle_input(PUZZLE_INPUT)
frequency = calculate_frequency(changes)
elapsed = round(time.process_time() - t, 4)

print(f'resulting frequency: {frequency}')
print(f'in {elapsed} seconds')

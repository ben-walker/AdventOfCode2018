PUZZLE_INPUT = 'day_5_input.txt'

def get_polymer(puzzle_file):
  with open(puzzle_file) as file_input:
    return file_input.readline().rstrip('\n')

polymer = get_polymer(PUZZLE_INPUT)

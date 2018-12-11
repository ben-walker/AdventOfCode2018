import itertools, time

PUZZLE_INPUT = 'day_2_input.txt'

def get_puzzle_input(puzzle_file):
  with open(puzzle_file) as file_input:
    return [line.rstrip('\n') for line in file_input]

def find_common_letters_for_correct_ids(box_ids):
  target_length = len(box_ids[0]) - 1
  for source, target in itertools.combinations(box_ids, 2):
    char_associations = list(zip(source, target))
    same_chars = [i[0] for i in char_associations if i[0] == i[1]]
    if len(same_chars) == target_length:
      return ''.join(same_chars)

t = time.process_time()
box_ids = get_puzzle_input(PUZZLE_INPUT)
common_letters = find_common_letters_for_correct_ids(box_ids)
elapsed = round(time.process_time() - t, 4)

print(f'common letters between the correct IDs: {common_letters}')
print(f'in {elapsed} seconds')

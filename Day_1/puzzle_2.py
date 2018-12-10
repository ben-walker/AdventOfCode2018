import itertools, time

PUZZLE_INPUT = 'day_1_input.txt'

def getPuzzleInput(puzzleFile):
  with open(puzzleFile) as fileInput:
    return [int(line.rstrip('\n')) for line in fileInput]

def findFirstDuplicate(changes):
  freq = 0
  found = set()
  for val in itertools.cycle(changes):
    freq += val
    if freq in found:
      return freq
    found.add(freq)

t = time.process_time()
puzzleInput = getPuzzleInput(PUZZLE_INPUT)
firstDuplicate = findFirstDuplicate(puzzleInput)
elapsed = round(time.process_time() - t, 4)

print(f'first duplicate frequency: {firstDuplicate}')
print(f'in {elapsed} seconds')

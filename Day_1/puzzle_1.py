import time

PUZZLE_INPUT = 'day_1_input.txt'

def getPuzzleInput(puzzleFile):
  with open(puzzleFile) as fileInput:
    return [int(line.rstrip('\n')) for line in fileInput]

def calculateFrequency(changes):
  return sum(changes)

t = time.process_time()
puzzleInput = getPuzzleInput(PUZZLE_INPUT)
frequency = calculateFrequency(puzzleInput)
elapsed = round(time.process_time() - t, 4)

print(f'resulting frequency: {frequency}')
print(f'in {elapsed} seconds')

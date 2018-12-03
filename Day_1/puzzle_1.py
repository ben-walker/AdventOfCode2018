PUZZLE_INPUT = 'day_1_input.txt'

def getPuzzleInput(puzzleFile):
  with open(puzzleFile) as fileInput:
    return [line.rstrip('\n') for line in fileInput]

def representInputAsNumeric(input):
  return [int(value) for value in input]

def calculateFrequency(changes):
  frequency = 0
  for change in changes:
    frequency += change
  return frequency

puzzleInput = getPuzzleInput(PUZZLE_INPUT)
numericInput = representInputAsNumeric(puzzleInput)
frequency = calculateFrequency(numericInput)

print(f'resulting frequency: {frequency}')

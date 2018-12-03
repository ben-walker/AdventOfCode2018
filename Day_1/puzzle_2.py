PUZZLE_INPUT = 'day_1_input.txt'

def getPuzzleInput(puzzleFile):
  with open(puzzleFile) as fileInput:
    return [line.rstrip('\n') for line in fileInput]

def representInputAsNumeric(input):
  return [int(value) for value in input]

def findFrequencyChanges(input, startingFrequency):
  changes = []
  for change in input:
    startingFrequency += change
    changes.append(startingFrequency)
  return changes

def updateSet(frequencySet, changes):
  for change in changes:
    if change in frequencySet:
      return change
    frequencySet.add(change)

foundFrequencies = set()
newFrequencies = []
firstDuplicate = None

puzzleInput = getPuzzleInput(PUZZLE_INPUT)
numericInput = representInputAsNumeric(puzzleInput)

while firstDuplicate == None:
  lastSeenFrequency = newFrequencies[-1] if newFrequencies else 0
  newFrequencies = findFrequencyChanges(numericInput, lastSeenFrequency)
  firstDuplicate = updateSet(foundFrequencies, newFrequencies)

print(f'first duplicate frequency: {firstDuplicate}')

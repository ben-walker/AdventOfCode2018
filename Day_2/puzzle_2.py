PUZZLE_INPUT = 'day_2_input.txt'

def getPuzzleInput(puzzleFile):
  with open(puzzleFile) as fileInput:
    return [line.rstrip('\n') for line in fileInput]

def getCommonLetters(source, target):
  common = ''
  for index, value in enumerate(source):
    if target[index] == value:
      common += value
  return common

def findCommonLettersForCorrectIDs(boxIDs):
  for index, idOne in enumerate(boxIDs):
    for idTwo in boxIDs[index:]:
      common = getCommonLetters(idOne, idTwo)
      if len(common) == len(idOne) - 1:
        return common

boxIDs = getPuzzleInput(PUZZLE_INPUT)
correctID = findCommonLettersForCorrectIDs(boxIDs)
print(f'common letters between the correct IDs: {correctID}')

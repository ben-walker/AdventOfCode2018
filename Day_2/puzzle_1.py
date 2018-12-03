PUZZLE_INPUT = 'day_2_input.txt'

def getPuzzleInput(puzzleFile):
  with open(puzzleFile) as fileInput:
    return [line.rstrip('\n') for line in fileInput]

def checkIdForDouble(boxID):
  for char in boxID:
    if boxID.count(char) == 2:
      return True
  return False

def checkIdForTriple(boxID):
  for char in boxID:
    if boxID.count(char) == 3:
      return True
  return False

def computeChecksum(boxIDs):
  numDoubles = 0
  numTriples = 0
  for ID in boxIDs:
    if checkIdForDouble(ID):
      numDoubles += 1
    if checkIdForTriple(ID):
      numTriples += 1
  return numDoubles * numTriples

boxIDs = getPuzzleInput(PUZZLE_INPUT)
print(f'checksum for box IDs: {computeChecksum(boxIDs)}')

import time
from collections import Counter

PUZZLE_INPUT = 'day_2_input.txt'

def getPuzzleInput(puzzleFile):
  with open(puzzleFile) as fileInput:
    return [line.rstrip('\n') for line in fileInput]

def computeChecksum(boxIDs):
  twosCount = 0
  threesCount = 0
  for id in boxIDs:
    commonLetters = Counter(id)
    commonCounts = commonLetters.values()
    if 2 in commonCounts: twosCount += 1
    if 3 in commonCounts: threesCount += 1
  return twosCount * threesCount

t = time.process_time()
boxIDs = getPuzzleInput(PUZZLE_INPUT)
checksum = computeChecksum(boxIDs)
elapsed = round(time.process_time() - t, 4)

print(f'checksum for box IDs: {checksum}')
print(f'in {elapsed} seconds')

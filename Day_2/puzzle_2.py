import itertools, time

PUZZLE_INPUT = 'day_2_input.txt'

def getPuzzleInput(puzzleFile):
  with open(puzzleFile) as fileInput:
    return [line.rstrip('\n') for line in fileInput]

def findCommonLettersForCorrectIDs(boxIDs):
  targetLength = len(boxIDs[0]) - 1
  for source, target in itertools.combinations(boxIDs, 2):
    charAssociations = list(zip(source, target))
    sameChars = [i[0] for i in charAssociations if i[0] == i[1]]
    if len(sameChars) == targetLength:
      return ''.join(sameChars)

t = time.process_time()
boxIDs = getPuzzleInput(PUZZLE_INPUT)
correctID = findCommonLettersForCorrectIDs(boxIDs)
elapsed = round(time.process_time() - t, 4)

print(f'common letters between the correct IDs: {correctID}')
print(f'in {elapsed} seconds')

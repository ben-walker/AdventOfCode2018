import numpy, re, time

PUZZLE_INPUT = 'day_3_input.txt'
SIDE_LENGTH = 1000

def getPuzzleInput(puzzleFile):
  with open(puzzleFile) as fileInput:
    claims = [line.rstrip('\n') for line in fileInput]
  return map(lambda claim: map(int, re.findall(r'\d+', claim)), claims)

def getInitialFabric(sideLength):
  return numpy.zeros((sideLength, sideLength))

def claimizeFabric(claims, fabric):
  for id, x, y, width, height in claims:
    fabric[x : x + width, y : y + height] += 1

def determineOverlaps(fabric):
  return len(numpy.where(fabric > 1)[0])

t = time.process_time()
fabric = getInitialFabric(SIDE_LENGTH)
claims = getPuzzleInput(PUZZLE_INPUT)
claimizeFabric(claims, fabric)
overlaps = determineOverlaps(fabric)
elapsed = round(time.process_time() - t, 4)

print(f'overlapping square inches of fabric: {overlaps}')
print(f'in {elapsed} seconds')

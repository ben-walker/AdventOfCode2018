import numpy, re, time

PUZZLE_INPUT = 'day_3_input.txt'
SIDE_LENGTH = 1000

def genClaims(claimFile):
  with open(claimFile) as fileInput:
    claims = [line.rstrip('\n') for line in fileInput]
  return map(lambda claim: map(int, re.findall(r'\d+', claim)), claims)

def getInitialFabric(sideLength):
  return numpy.zeros((sideLength, sideLength))

def claimizeFabric(fabric):
  for id, x, y, width, height in genClaims(PUZZLE_INPUT):
    fabric[x : x + width, y : y + height] += 1

def findNonOverlappingClaim(claimizedFabric):
  for id, x, y, width, height in genClaims(PUZZLE_INPUT):
    if numpy.all(claimizedFabric[x : x + width, y : y + height] == 1):
      return id

t = time.process_time()
fabric = getInitialFabric(SIDE_LENGTH)
claimizeFabric(fabric)
targetID = findNonOverlappingClaim(fabric)
elapsed = round(time.process_time() - t, 4)

print(f'non-overlapping claim ID: {targetID}')
print(f'in {elapsed} seconds')

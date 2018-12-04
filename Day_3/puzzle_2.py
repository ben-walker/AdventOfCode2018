import numpy
import re

PUZZLE_INPUT = 'day_3_input.txt'
SIDE_LENGTH = 1000
HAS_OVERLAPS = {}

FREE = 0
OVERLAP = -1

def getPuzzleInput(puzzleFile):
  with open(puzzleFile) as fileInput:
    return [line.rstrip('\n') for line in fileInput]

def getInitialFabric(sideLength):
  return numpy.zeros((SIDE_LENGTH, SIDE_LENGTH), numpy.int32)

def getClaimCoords(claim):
  pattern = '#.* @ (.*): .*'
  rawCoords = re.search(pattern, claim).group(1).split(',')
  return tuple([int(i) for i in rawCoords])

def getClaimSize(claim):
  pattern = '#.* @ .*: (.*)'
  rawSize = re.search(pattern, claim).group(1).split('x')
  return tuple([int(i) for i in rawSize])

def getClaimID(claim):
  pattern = '#(.*) @ .*: .*'
  return int(re.search(pattern, claim).group(1))

def updateOverlapTracker(claimID, patch):
  HAS_OVERLAPS[claimID] = True
  if patch in HAS_OVERLAPS:
    HAS_OVERLAPS[patch] = True

def updateFabric(fabric, coords, size, id):
  x = coords[0]
  y = coords[1]
  width = size[0]
  height = size[1]

  HAS_OVERLAPS[id] = False
  for i in range(y, y + height):
    for j in range(x, x + width):
      patch = fabric[i][j]
      if patch != FREE: updateOverlapTracker(id, patch)
      fabric[i][j] = id if patch == FREE else OVERLAP

def claimizeFabric(claims, fabric):
  for claim in claims:
    coords = getClaimCoords(claim)
    size = getClaimSize(claim)
    id = getClaimID(claim)
    updateFabric(fabric, coords, size, id)

def findNonOverlappingClaim():
  return list(HAS_OVERLAPS.keys())[list(HAS_OVERLAPS.values()).index(False)]

fabric = getInitialFabric(SIDE_LENGTH)
claims = getPuzzleInput(PUZZLE_INPUT)
claimizeFabric(claims, fabric)
print(f'non-overlapping claim ID: {findNonOverlappingClaim()}')

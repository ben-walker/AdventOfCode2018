import numpy
import re

PUZZLE_INPUT = 'day_3_input.txt'
SIDE_LENGTH = 1000

CLAIM = '#'
FREE = '.'
OVERLAP = 'X'

def getPuzzleInput(puzzleFile):
  with open(puzzleFile) as fileInput:
    return [line.rstrip('\n') for line in fileInput]

def getInitialFabric(sideLength):
  return numpy.full((SIDE_LENGTH, SIDE_LENGTH), FREE)

def getClaimCoords(claim):
  '''
  Return a tuple holding the starting coordinates of
  the claim, with the form:
  (X inches from the left, Y inches from the top)
  '''
  pattern = '#.* @ (.*): .*'
  rawCoords = re.search(pattern, claim).group(1).split(',')
  return tuple([int(i) for i in rawCoords])

def getClaimSize(claim):
  '''
  Return a tuple holding the size of the claim,
  with the form:
  (inches wide, inches tall)
  '''
  pattern = '#.* @ .*: (.*)'
  rawSize = re.search(pattern, claim).group(1).split('x')
  return tuple([int(i) for i in rawSize])

def updateFabric(fabric, startX, startY, width, height):
  '''
  On completion, fabric will be a numpy 2D array with
  the following properties:
  - '.' denotes an unclaimed square inch
  - '#' denotes a square inch claimed once
  - 'X' denotes a square inch claimed multiple times (overlap)
  '''
  for i in range(startY, startY + height):
    for j in range(startX, startX + width):
      patch = fabric[i][j]
      fabric[i][j] = CLAIM if patch == FREE else OVERLAP

def claimizeFabric(claims, fabric):
  for claim in claims:
    coords = getClaimCoords(claim)
    size = getClaimSize(claim)
    updateFabric(fabric, coords[0], coords[1], size[0], size[1])

def determineOverlaps(fabric):
  unique, counts = numpy.unique(fabric, return_counts = True)
  fabricCounts = dict(zip(unique, counts))
  return fabricCounts.get(OVERLAP)

fabric = getInitialFabric(SIDE_LENGTH)
claims = getPuzzleInput(PUZZLE_INPUT)
claimizeFabric(claims, fabric)
print(f'overlapping square inches of fabric: {determineOverlaps(fabric)}')

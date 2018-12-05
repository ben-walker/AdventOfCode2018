from Guard import Guard
import re

PUZZLE_INPUT = 'day_4_input.txt'

def getPuzzleInput(puzzleFile):
  with open(puzzleFile) as fileInput:
    return [line.rstrip('\n') for line in fileInput]

def newGuard(id, guards):
  guards.append(Guard(id))

def startShift(record, guards):
  pattern = 'Guard #(.*) begins'
  guardId = int(re.search(pattern, record).group(1))
  if not any(x.id == guardId for x in guards):
    newGuard(guardId, guards)
  guard = next(x for x in guards if x.id == guardId)
  

def processRecords(chronoRecords, guards):
  for record in chronoRecords:
    if 'shift' in record:
      startShift(record, guards)

guards = []
chronoRecords = sorted(getPuzzleInput(PUZZLE_INPUT))
processRecords(chronoRecords, guards)

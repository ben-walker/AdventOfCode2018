import re, time
from collections import defaultdict

PUZZLE_INPUT = 'day_4_input.txt'

def getSortedTimesheet(puzzleFile):
  with open(puzzleFile) as fileInput:
    return sorted([line.rstrip('\n') for line in fileInput])

def updateGuardAsleepMinutes(guardTracker, id, rangeGen):
  for i in rangeGen:
    guardTracker[id][i] += 1

def processTimesheet(timesheet):
  sleepTracker = defaultdict(int)
  guardTracker = defaultdict(lambda: defaultdict(int))
  for log in timesheet:
    action = re.findall(r'] (.*)', log)[0]
    if action.startswith('Guard'):
      guardID = int(re.findall(r'#(\d+)', log)[0])
    elif action.startswith('falls asleep'):
      fellAsleep = int(re.findall(r':(\d+)', log)[0])
    elif action.startswith('wakes up'):
      wokeUp = int(re.findall(r':(\d+)', log)[0])
      sleepTracker[guardID] += wokeUp - fellAsleep
      updateGuardAsleepMinutes(guardTracker, guardID, range(fellAsleep, wokeUp))
  return sleepTracker, guardTracker

def getSleepiestGuardID(sleepTracker):
  return max(sleepTracker, key = lambda i: sleepTracker[i])

def getSleepiestMinuteForGuard(guardTracker, sleepiestGuard):
  return max(guardTracker[sleepiestGuard], key = lambda i: guardTracker[sleepiestGuard][i])

t = time.process_time()
timesheet = getSortedTimesheet(PUZZLE_INPUT)
sleepTracker, guardTracker = processTimesheet(timesheet)
sleepiestGuard = getSleepiestGuardID(sleepTracker)
sleepiestMinute = getSleepiestMinuteForGuard(guardTracker, sleepiestGuard)
answer = sleepiestGuard * sleepiestMinute
elapsed = round(time.process_time() - t, 4)

print(f'id x minute: {answer}')
print(f'in {elapsed} seconds')

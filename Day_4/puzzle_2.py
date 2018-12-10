import re, time
from collections import defaultdict

PUZZLE_INPUT = 'day_4_input.txt'

def get_sorted_timesheet(puzzle_file):
  with open(puzzle_file) as file_input:
    return sorted([line.rstrip('\n') for line in file_input])

def update_guard_asleep_minutes(guard_tracker, id, range_gen):
  for i in range_gen:
    guard_tracker[id][i] += 1

def process_timesheet(timesheet):
  guard_tracker = defaultdict(lambda: defaultdict(int))
  for log in timesheet:
    action = re.findall(r'] (.*)', log)[0]
    if action.startswith('Guard'):
      guard_id = int(re.findall(r'#(\d+)', log)[0])
    elif action.startswith('falls asleep'):
      fell_asleep = int(re.findall(r':(\d+)', log)[0])
    elif action.startswith('wakes up'):
      woke_up = int(re.findall(r':(\d+)', log)[0])
      update_guard_asleep_minutes(guard_tracker, guard_id, range(fell_asleep, woke_up))
  return guard_tracker

def most_slept_on_product(guard_tracker):
  sleepiest_minute = 0
  for guard in guard_tracker:
    for minute in guard_tracker[guard]:
      if guard_tracker[guard][minute] > sleepiest_minute:
        sleepiest_minute = guard_tracker[guard][minute]
        sleep_prod = guard * minute
  return sleep_prod

t = time.process_time()
timesheet = get_sorted_timesheet(PUZZLE_INPUT)
guard_tracker = process_timesheet(timesheet)
product = most_slept_on_product(guard_tracker)
elapsed = round(time.process_time() - t, 4)

print(f'id x minute: {product}')
print(f'in {elapsed} seconds')

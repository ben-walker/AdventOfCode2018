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
  sleep_tracker = defaultdict(int)
  guard_tracker = defaultdict(lambda: defaultdict(int))
  for log in timesheet:
    action = re.findall(r'] (.*)', log)[0]
    if action.startswith('Guard'):
      guard_id = int(re.findall(r'#(\d+)', log)[0])
    elif action.startswith('falls asleep'):
      fell_asleep = int(re.findall(r':(\d+)', log)[0])
    elif action.startswith('wakes up'):
      woke_up = int(re.findall(r':(\d+)', log)[0])
      sleep_tracker[guard_id] += woke_up - fell_asleep
      update_guard_asleep_minutes(guard_tracker, guard_id, range(fell_asleep, woke_up))
  return sleep_tracker, guard_tracker

def get_sleepiest_guard_id(sleep_tracker):
  return max(sleep_tracker, key = lambda i: sleep_tracker[i])

def get_sleepiest_minute_for_guard(guard_tracker, guard_id):
  return max(guard_tracker[guard_id], key = lambda i: guard_tracker[guard_id][i])

t = time.process_time()
timesheet = get_sorted_timesheet(PUZZLE_INPUT)
sleep_tracker, guard_tracker = process_timesheet(timesheet)
sleepiest_guard = get_sleepiest_guard_id(sleep_tracker)
sleepiest_minute = get_sleepiest_minute_for_guard(guard_tracker, sleepiest_guard)
answer = sleepiest_guard * sleepiest_minute
elapsed = round(time.process_time() - t, 4)

print(f'id x minute: {answer}')
print(f'in {elapsed} seconds')

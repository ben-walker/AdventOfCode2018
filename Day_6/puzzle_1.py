import time

PUZZLE_INPUT = 'day_6_input.txt'

def get_points(puzzle_file):
  with open(puzzle_file) as file_input:
    points = [line.rstrip('\n') for line in file_input]
  return map(lambda point: map(int, point.split(', ')), points)

points = get_points(PUZZLE_INPUT)

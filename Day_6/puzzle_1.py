import time

PUZZLE_INPUT = 'day_6_input.txt'

def get_points(puzzle_file):
  with open(puzzle_file) as file_input:
    points = [line.rstrip('\n') for line in file_input]
  return [tuple(map(int, point.split(', '))) for point in points]

def calc_manhattan(M, P):
  Mx, My = M
  Px, Py = P
  return abs(Mx - Px) + abs(My - Py)

points = get_points(PUZZLE_INPUT)

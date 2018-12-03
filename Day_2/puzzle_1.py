PUZZLE_INPUT = 'day_2_input.txt'

def getPuzzleInput(puzzleFile):
  with open(puzzleFile) as fileInput:
    return [line.rstrip('\n') for line in fileInput]

print(getPuzzleInput(PUZZLE_INPUT))

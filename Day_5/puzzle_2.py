import time

PUZZLE_INPUT = 'day_5_input.txt'

def get_polymer(puzzle_file):
  with open(puzzle_file) as file_input:
    return file_input.readline().rstrip('\n')

def extract_agents(polymer):
  return list(set(polymer.lower()))

def polarity_reversed(uOne, uTwo):
  if uOne is None or uTwo is None: return False
  return (
    uOne.lower() == uTwo.lower() and (
      (uOne.isupper() and uTwo.islower()) or
      (uOne.islower() and uTwo.isupper())
    )
  )

def remove_reactive_units(polymer):
  i = 0
  while i < len(polymer):
    unit = polymer[i]
    next_unit = polymer[i + 1] if i < len(polymer) - 1 else None
    if polarity_reversed(unit, next_unit):
      polymer = polymer[: i] + polymer[i + 2 :]
      i = max(i - 1, 0)
      continue
    i += 1
  return polymer

def find_shortest_polymer_length(agents, polymer):
  shortest = len(polymer)
  for agent in agents:
    non_agent_polymer = polymer.replace(agent, '').replace(agent.upper(), '')
    length = len(remove_reactive_units(non_agent_polymer))
    shortest = min(shortest, length)
  return shortest

t = time.process_time()
polymer = get_polymer(PUZZLE_INPUT)
agents = extract_agents(polymer)
shortest = find_shortest_polymer_length(agents, polymer)
elapsed = round(time.process_time() - t, 4)

print(f'shortest produced polymer: {shortest}')
print(f'in {elapsed} seconds')

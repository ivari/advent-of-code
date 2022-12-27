from queue import PriorityQueue

with open('input.txt') as f:
  input_lines = f.read().splitlines()

entry = (0, 1) # (0, 1)
outry = (26, 120) # (6, 5) (5, 6), (26, 120)

if outry[0] != len(input_lines) - 1:
  raise Exception('Wrong exit condition')

valley = []
for row in input_lines:
  valley.append(list(row))

def grid(valley, entry):
  for i in range(len(valley)):
    row = list(valley[i])

    if i == entry[0]:
      row[entry[1]] = 'E'

    print(row)

  print()

def wind(valley):
  nvalley = [['' for _ in row] for row in valley]

  for i in range(len(valley)):
    for j in range(len(valley[i])):
      sq = valley[i][j]

      for k in range(len(sq)):
        current = sq[k]

        if current == '#':
          nvalley[i][j] = current

        elif current == '>':
          if valley[i][j+1] == '#':
            nvalley[i][1] += current
          else:
            nvalley[i][j+1] += current

        elif current == 'v':
          if valley[i+1][j] == '#':
            nvalley[1][j] += current
          else:
            nvalley[i+1][j] += current

        elif current == '<':
          if valley[i][j-1] == '#':
            nvalley[i][len(nvalley[i])-2] += current
          else:
            nvalley[i][j-1] += current

        elif current == '^':
          if valley[i-1][j] == '#':
            nvalley[len(nvalley)-2][j] += current
          else:
            nvalley[i-1][j] += current

  return nvalley

def is_retry(valley, exped, steps, tried):
  if exped not in tried:
    return False

  for r in tried[exped]:
    v, s = r
    if v == valley and s <= steps:
      return True

  return False

def process(valley, exped, limit = 300):
  global outry, section

  paths = [limit]
  tried = {}

  stack = PriorityQueue()
  stack.put((1, (valley, exped, 0)))

  base_prio = len(valley) + len(valley[0])

  while not stack.empty():
    valley, exped, steps = stack.get()[1]
    steps += 1

    fri, frj = exped
    distance = abs(outry[0] - fri) + abs(outry[1] - frj)

    print(section, stack.qsize(), len(tried), steps, distance, min(paths))

    # if too long already, stop
    if min(paths) < steps + distance:
      continue

    for move in ((0, 0), (0, 1), (1, 0), (0, -1), (-1, 0)):
      # move expedition
      toi, toj = fri + move[0], frj + move[1]

      # if out of bounds, stop
      if toi < 0 or toj < 0 or len(valley) <= toi or len(valley[toi]) <= toj:
        continue

      # move blizzards
      nvalley = wind(valley)

      # if cannot move to target, stop
      if nvalley[toi][toj] != '':
        continue

      # if this state has already happened, stop
      if is_retry(nvalley, (toi, toj), steps, tried):
        continue

      # if at end and shortest path, add to paths
      if (toi, toj) == outry and steps < min(paths):
        paths.append(steps)

      # add current state to stack
      prio = base_prio - (abs(outry[0] - fri) + abs(outry[1] - frj))
      stack.put((prio, (nvalley, (toi, toj), steps)))

      # add current state to history
      ind = toi, toj
      if ind not in tried:
        tried[ind] = []
      tried[ind].append((nvalley, steps))

  return min(paths)

section = 1
minutes1 = process(valley, entry)
# minutes1 = 281

for _ in range(minutes1):
  valley = wind(valley)
entry, outry = outry, entry

section = 2
minutes2 = process(valley, entry)
# minutes2 = 242

for _ in range(minutes2):
  valley = wind(valley)
entry, outry = outry, entry

section = 3
minutes3 = process(valley, entry)
# minutes3 = 284

print()
print(
  'Totals:',
  minutes1,
  minutes2,
  minutes3,
  minutes1 + minutes2 + minutes3
)

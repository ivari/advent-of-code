def main():
  with open('input.txt') as f:
    input_lines = f.read().splitlines()

  # part 1

  print('Attempting part 1')
  print()

  grove = [list(row) for row in input_lines]
  grid(grove)

  for r in range(10):
    grove, _ = process(grove, r + 1)
    grid(grove)

  grove = trim(grove)
  grid(grove)

  part1 = empties(grove)

  # part 2

  print('Attempting part 2')
  print()

  grove = [list(row) for row in input_lines]
  grid(grove)

  r = 0
  while True:
    grove, moves = process(grove, r + 1)
    grid(grove)

    if moves == 0:
      break

    r += 1

  part2 = r + 1

  # display results

  print('Part 1 answer:', part1)
  print('Part 2 answer:', part2)

def process(grove, r = 1):
  moves = {}
  prios = ['north', 'south', 'west', 'east']
  prios = (prios * 2)[(r - 1)%4:(r - 1)%4+4]

  for i in range(len(grove)):
    for j in range(len(grove[i])):
      if grove[i][j] == '.':
        continue

      # go nowhere
      if not has_elf(grove, i - 1, j - 1) and not has_elf(grove, i - 1, j) \
        and not has_elf(grove, i - 1, j + 1) and not has_elf(grove, i, j - 1) \
        and not has_elf(grove, i, j + 1) and not has_elf(grove, i + 1, j - 1) \
        and not has_elf(grove, i + 1, j) and not has_elf(grove, i + 1, j + 1):
        continue

      for prio in prios:
        # go north
        if prio == 'north':
          if has_elf(grove, i - 1, j - 1) \
            or has_elf(grove, i - 1, j) \
            or has_elf(grove, i - 1, j + 1):
            continue

          k = i - 1, j
          if k not in moves:
            moves[k] = []

          moves[k].append((i, j))
          break

        # go south
        if prio == 'south':
          if has_elf(grove, i + 1, j - 1) \
            or has_elf(grove, i + 1, j) \
            or has_elf(grove, i + 1, j + 1):
            continue

          k = i + 1, j
          if k not in moves:
            moves[k] = []

          moves[k].append((i, j))
          break

        # go west
        if prio == 'west':
          if has_elf(grove, i - 1, j - 1) \
            or has_elf(grove, i, j - 1) \
            or has_elf(grove, i + 1, j - 1):
            continue

          k = i, j - 1
          if k not in moves:
            moves[k] = []

          moves[k].append((i, j))
          break

        # go east
        if prio == 'east':
          if has_elf(grove, i - 1, j + 1) \
            or has_elf(grove, i, j + 1) \
            or has_elf(grove, i + 1, j + 1):
            continue

          k = i, j + 1
          if k not in moves:
            moves[k] = []

          moves[k].append((i, j))
          break

  bfi, bfj = 0, 0
  for to in moves:
    if 1 < len(moves[to]):
      continue

    grove, bfi, bfj = move_elf(
      grove,
      moves[to][0],
      to,
      bfi,
      bfj
    )

  return grove, len(moves)

def move_elf(grove, fr, to, bfi, bfj):
  fri, frj = fr[0] + bfi, fr[1] + bfj
  toi, toj = to[0] + bfi, to[1] + bfj

  while toi < 0:
    grove = [['.' for _ in grove[0]]] + grove

    fri += 1
    toi += 1
    bfi += 1

  while toj < 0:
    for i in range(len(grove)):
      grove[i] = ['.'] + grove[i]

    frj += 1
    toj += 1
    bfj += 1

  while len(grove) <= toi:
    grove.append(['.' for _ in grove[0]])

  while len(grove[toi]) <= toj:
    for i in range(len(grove)):
      grove[i].append('.')

  grove[fri][frj], grove[toi][toj] = '.', grove[fri][frj]

  return grove, bfi, bfj

def has_elf(grove, i, j):
  if i < 0 or j < 0:
    return False

  try:
    return grove[i][j] == '#'
  except IndexError:
    return False

def trim(grove):
  # check top
  done = False
  while not done:
    for x in grove[0]:
      if x == '#':
        done = True
        break
    else:
      grove.pop(0)

  # check bottom
  done = False
  while not done:
    for x in grove[-1]:
      if x == '#':
        done = True
        break
    else:
      grove.pop()

  # check left
  done = False
  while not done:
    for i in range(len(grove)):
      if grove[i][0] == '#':
        done = True
        break
    else:
      for i in range(len(grove)):
        grove[i].pop(0)

  # check right
  done = False
  while not done:
    for i in range(len(grove)):
      if grove[i][-1] == '#':
        done = True
        break
    else:
      for i in range(len(grove)):
        grove[i].pop()

  return grove

def empties(grove):
  total = 0

  for i in range(len(grove)):
    for j in range(len(grove[i])):
      if grove[i][j] == '.':
        total += 1

  return total

def grid(grove):
  for row in grove:
    print(''.join(row))

  print()

main()

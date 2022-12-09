def main():
  data = read_file_to_list()

  two_knots = process(data)
  ten_knots = process(data, 10)

  print(two_knots)
  print(ten_knots)

def read_file_to_list():
  with open('input.txt') as f:
    content = f.read().splitlines()

  return content

def process(data, rope_size = 2):
  knots = []
  for k in range(rope_size):
    knots.append([0, 0])

  visited = set()
  visited.add('%s,%s' % tuple(knots[-1]))

  for i in range(len(data)):
    bits             = data[i].split(' ')
    direction, steps = bits[0], int(bits[1])

    for s in range(steps):
      if direction == 'U':
        knots[0] = [knots[0][0], knots[0][1] + 1]

      elif direction == 'D':
        knots[0] = [knots[0][0], knots[0][1] - 1]

      elif direction == 'L':
        knots[0] = [knots[0][0] - 1, knots[0][1]]

      elif direction == 'R':
        knots[0] = [knots[0][0] + 1, knots[0][1]]

      for k in range(1, len(knots)):
        prev = knots[k - 1]
        curr = knots[k]

        # same column
        if prev[0] == curr[0] and 1 < abs(prev[1] - curr[1]):
          knots[k][1] += 1 if prev[1] > curr[1] else -1

        # same row
        elif prev[1] == curr[1] and 1 < abs(prev[0] - curr[0]):
          knots[k][0] += 1 if prev[0] > curr[0] else -1

        # diagonal
        elif 1 < abs(prev[0] - curr[0]) or 1 < abs(prev[1] - curr[1]):
          knots[k][0] += 1 if prev[0] > curr[0] else -1
          knots[k][1] += 1 if prev[1] > curr[1] else -1

      visited.add('%s,%s' % tuple(knots[-1]))

  return len(visited)


main()

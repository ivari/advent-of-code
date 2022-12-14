import functools

def main():
  data     = read_file_to_list()

  without_floor = process(data)
  with_floor    = process(data, True)

  print('Part 1 result:', without_floor)
  print('Part 2 result:', with_floor)

def read_file_to_list():
  with open('input.txt') as f:
    content = f.read().splitlines()

  return content

def process(data, floor = False):
  grid   = [['.']]
  margin = { 'x': None }

  # grid

  for line in data:
    bits = line.split(' -> ')

    previous = None
    for location in bits:
      location = location.split(',')
      location = int(location[0]), int(location[1])

      if previous == None:
        previous = location
        continue

      px, py = previous
      cx, cy = location

      if margin['x'] == None:
        margin['x'] = px

      minx = min(px, cx)
      if minx < margin['x']:
        for i in range(len(grid)):
          grid[i] = ['.'] * (margin['x'] - minx) + grid[i]
        margin['x'] = minx

      px -= margin['x']
      cx -= margin['x']

      for x in range(len(grid[0]), max(px, cx) + 1):
        for y in range(len(grid)):
          grid[y].append('.')

      for y in range(len(grid), max(py, cy) + 1):
        grid.append(['.'] * len(grid[0]))

      if px == cx:
        for y in range(min(py, cy), max(py, cy) + 1):
          grid[y][cx] = '#'

      if py == cy:
        for x in range(min(px, cx), max(px, cx) + 1):
          grid[cy][x] = '#'

      previous = location

  # print_grid(grid)

  # sand

  if floor:
    grid.append(['.'] * len(grid[0]))
    grid.append(['#'] * len(grid[0]))
    # print_grid(grid)

  sands = 0
  void  = False
  while not void:
    sx, sy = 500 - margin['x'], 0

    while True:
      if out_of_bounds(sy + 1, sx, grid, floor, margin):
        if floor:
          raise 'Fell through the floor'
        void = True
        break
      if grid[sy+1][sx] == '.':
        sy += 1
        continue

      if out_of_bounds(sy + 1, sx - 1, grid, floor, margin):
        void = True
        break
      if floor and sx - 1 < 0:
        sx += 1
      if grid[sy+1][sx-1] == '.':
        sy += 1
        sx -= 1
        continue

      if out_of_bounds(sy + 1, sx + 1, grid, floor, margin):
        void = True
        break
      if grid[sy+1][sx+1] == '.':
        sy += 1
        sx += 1
        continue

      if sx == 500 - margin['x'] and sy == 0:
        void = True

      grid[sy][sx] = 'o'
      sands += 1
      break

  # print_grid(grid)
  return sands

def out_of_bounds(sy, sx, grid, floor, margin):
  return oob_top(sy) \
    or oob_bottom(sy, grid) \
    or oob_left(sx, grid, floor, margin) \
    or oob_right(sx, grid, floor)

def oob_top(sy):
  return sy < 0

def oob_bottom(sy, grid):
  return len(grid) <= sy

def oob_left(sx, grid, floor, margin):
  result = sx < 0

  if floor and result:
    for i in range(len(grid)):
      grid[i] = ['.'] + grid[i]

    grid[len(grid)-1][0] = '#'

    margin['x'] -= 1

    return False

  return result

def oob_right(sx, grid, floor):
  result = len(grid[0]) <= sx

  if floor and result:
    for i in range(len(grid)):
      grid[i].append('.')

    grid[len(grid)-1][len(grid[0])-1] = '#'

    return False

  return result

def print_grid(grid):
  print()

  for line in grid:
    print(''.join(line))

  print()

main()

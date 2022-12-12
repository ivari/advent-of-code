def main():
  data   = read_file_to_list()

  from_start = process(data, [20, 0])
  print('Total paths:', from_start[0])
  print('Least steps from "S":', from_start[1])

  any_start = process(data)
  print('Total paths:', any_start[0])
  print('Least steps from any "a":', any_start[1])

def read_file_to_list():
  with open('input.txt') as f:
    content = f.read().splitlines()

  return content

def process(data, start = None):
  stack     = [[start]]
  completed = []
  visited   = {}

  if start == None:
    stack   = build_start(data)
  elif data[start[0]][start[1]] != 'S':
    raise AttributeError('Starting location is not correct')

  move(stack, completed, data, visited)

  return (
    len(completed),
    min(list(map(len, completed))) - 1
  )

def build_start(data):
  stack = []

  for i in range(len(data)):
    for j in range(len(data[0])):
      is_side = i == 0 or j == 0 or i == len(data) - 1 or j == len(data[0]) - 1

      if is_side and (data[i][j] == 'a' or data[i][j] == 'S'):
        stack.append([[i, j]])

  return stack

def move(stack, completed, data, visited):
  wi, wj = len(data), len(data[0])
  stats  = {
    'moves':     0,
    'stack':     0,
    'latest':    0,
    'completed': 0
  }

  while 0 < len(stack):
    path   = stack.pop(0)
    fr     = path[-1]
    ci, cj = fr

    stats['moves']     += 1
    stats['stack']     = len(stack)
    stats['latest']    = len(stack[-1]) if 0 < len(stack) else 0
    stats['completed'] = len(completed)
    if stats['moves'] % 1000 == 0:
      print(stats)

    for mi, mj in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
      ni, nj = ci + mi, cj + mj
      to     = [ni, nj]

      if out_of_bounds(ni, nj, wi, wj):
        continue

      if have_been_at(ni, nj, path):
        continue

      if too_high(fr, to, data):
        continue

      npath = list(path)
      npath.append(to)

      if at_elevation(to, data):
        completed.append(npath)
        continue

      to_str = str(ni) + ',' + str(nj)
      if to_str not in visited or len(npath) < visited[to_str]:
        stack.append(npath)
        visited[to_str] = len(npath)

def out_of_bounds(i, j, wi, wj):
  return i < 0 or j < 0 or wi <= i or wj <= j

def have_been_at(i, j, path):
  return [i, j] in path

def too_high(fr, to, data):
  fri, frj   = fr
  toi, toj   = to
  vfr, vto   = data[fri][frj], data[toi][toj]

  from_start = vfr == 'S'
  to_peak    = (vfr == 'y' or vfr == 'z') and vto == 'E'
  can_reach  = vto != 'E' and ord(vto) - ord(vfr) <= 1

  return not (from_start or to_peak or can_reach)

def at_elevation(to, data):
  toi, toj = to
  vto      = data[toi][toj]

  return vto == 'E'

main()

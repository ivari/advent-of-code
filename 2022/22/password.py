import re

def main():
  with open('input.txt') as f:
    input_lines = f.read().splitlines()

  board = []
  moves = False
  for row in input_lines:
    if row == '':
      moves = True

    elif moves:
      moves = []
      for m in re.compile('\d+[RL]').findall(row):
        moves.append(int(m[:-1]))
        moves.append(m[-1])

      if row[-1] != str(moves[-1])[-1]:
        for i in range(len(row) - 1, -1, -1):
          if row[i] == 'L' or row[i] == 'R':
            moves.append(int(row[i+1:]))
            break

    else:
      board.append(list(row))

  # for x in board:
  #   print(x)
  # print()
  # print(moves)
  # print()

  part1 = process(board, moves)
  part2 = process(board, moves, True)

  print('Part 1 result:', part1)
  print('Part 2 result:', part2)

def process(board, moves, cube_it = False, prod = True):
  pos = 0, 0
  direction = 0

  i, j = pos
  while board[i][j] == ' ':
    j += 1
  pos = i, j

  wraps = wrap_cube(board, prod) if cube_it else wrap_linear(board)

  for m in moves:
    print('Move:', m)

    i, j = pos

    if isinstance(m, str):
      print('Turning:', pos, ['>', 'v', '<', '^'][direction])

      if m == 'R':
        direction += 1

      if m == 'L':
        direction -= 1

      direction %= 4

      print('Turned:', pos, ['>', 'v', '<', '^'][direction])

    if isinstance(m, int):
      while 0 < m:
        try:
          if direction == 0:
            ntile = board[i][j+1]

            if ntile == ' ':
              raise IndexError('board position out of range')

            if ntile == '.':
              j += 1
              m -= 1
              pos = i, j

            if ntile == '#':
              m = 0

          if direction == 1:
            ntile = board[i+1][j]

            if ntile == ' ':
              raise IndexError('board position out of range')

            if ntile == '.':
              i += 1
              m -= 1
              pos = i, j

            if ntile == '#':
              m = 0

          if direction == 2:
            if j - 1 < 0:
              raise IndexError('board position out of range')

            ntile = board[i][j-1]

            if ntile == ' ':
              raise IndexError('board position out of range')

            if ntile == '.':
              j -= 1
              m -= 1
              pos = i, j

            if ntile == '#':
              m = 0

          if direction == 3:
            if i - 1 < 0:
              raise IndexError('board position out of range')

            ntile = board[i-1][j]

            if ntile == ' ':
              raise IndexError('board position out of range')

            if ntile == '.':
              i -= 1
              m -= 1
              pos = i, j

            if ntile == '#':
              m = 0

        except IndexError:
          before = direction

          if direction in [0, 2]:
            i, j, direction = wraps[direction][i]
          elif direction in [1, 3]:
            i, j, direction = wraps[direction][j]

          if direction == 0:
            while True:
              try:
                if board[i][j] == ' ':
                  j += 1
                else:
                  break
              except IndexError:
                j += 1

            if board[i][j] == '#':
              m = 0
              direction = before
              break

            m -= 1
            pos = i, j

          if direction == 1:
            while True:
              try:
                if board[i][j] == ' ':
                  i += 1
                else:
                  break
              except IndexError:
                i += 1

            if board[i][j] == '#':
              m = 0
              direction = before
              break

            m -= 1
            pos = i, j

          if direction == 2:
            while True:
              try:
                if board[i][j] == ' ':
                  j -= 1
                else:
                  break
              except IndexError:
                j -= 1

            if board[i][j] == '#':
              m = 0
              direction = before
              break

            m -= 1
            pos = i, j

          if direction == 3:
            while True:
              try:
                if board[i][j] == ' ':
                  i -= 1
                else:
                  break
              except IndexError:
                i -= 1

            if board[i][j] == '#':
              m = 0
              direction = before
              break

            m -= 1
            pos = i, j

      print('Moved:', ['>', 'v', '<', '^'][direction], pos)
      # paround(board, pos[0], pos[1])
      # pfull(board, pos[0], pos[1], direction)

    print()

  print('End:', pos)

  return 1000 * (pos[0] + 1) + 4 * (pos[1] + 1) + direction

def wrap_linear(board):
  wrap = {
    0: {},
    1: {},
    2: {},
    3: {}
  }

  for i in range(len(board)):
    wrap[0][i] = i, 0, 0
    wrap[2][i] = i, len(board[i]) - 1, 2

    for j in range(len(board[i])):
      wrap[1][j] = 0, j, 1
      wrap[3][j] = len(board) - 1, j, 3

  return wrap

def wrap_cube(board, prod = True):
  if not prod:
    return wrap_cube_sample()

  sqlen = 50
  height = len(board)
  width = len(board[0])

  edges = {
                            (1, 2): {
                              2: (3, 1, 0, False),
                              3: (4, 1, 0, True)
                            },                      (1, 3): {
                                                      0: (3, 2, 2, False),
                                                      1: (2, 2, 2, True),
                                                      3: (4, 1, 3, True)
                                                    },
    # -------------------------------------------------------------
                            (2, 2): {
                              0: (1, 3, 3, True),
                              2: (3, 1, 1, True)
                            },
    # -------------------------------------------------------------
    (3, 1): {
      2: (1, 2, 0, False),
      3: (2, 2, 0, True)
    },                      (3, 2): {
                              0: (1, 3, 2, False),
                              1: (4, 1, 2, True)
                            },
    # -------------------------------------------------------------
    (4, 1): {
      0: (3, 2, 3, True),
      1: (1, 3, 1, True),
      2: (1, 2, 1, True)
    }
  }

  wraps = {}

  for sq in edges:
    sqx, sqy = sq

    for direction in edges[sq]:
      if direction not in wraps:
        wraps[direction] = {}

      print('Parsing:', sq, direction, edges[sq][direction])

      if direction in (0, 2):
        for i in range((sqx - 1) * sqlen, sqx * sqlen):
          wraps[direction][i] = build_target(edges[sq][direction], i, sqlen)
          print(i, wraps[direction][i])

      if direction in (1, 3):
        for j in range((sqy - 1) * sqlen, sqy * sqlen):
          wraps[direction][j] = build_target(edges[sq][direction], j, sqlen)
          print(j, wraps[direction][j])

  return wraps

def build_target(data, coord, sqlen):
  nsqx, nsqy, ndirection, nsame = data
  coord %= sqlen

  if ndirection == 0:
    toj = (nsqy - 1) * sqlen
    if nsame:
      toi = (nsqx - 1) * sqlen + coord
    else:
      toi = nsqx * sqlen - 1 - coord

  if ndirection == 1:
    toi = (nsqx - 1) * sqlen
    if nsame:
      toj = (nsqy - 1) * sqlen + coord
    else:
      toj = nsqy * sqlen - 1 - coord

  if ndirection == 2:
    toj = nsqy * sqlen - 1
    if nsame:
      toi = (nsqx - 1) * sqlen + coord
    else:
      toi = nsqx * sqlen - 1 - coord

  if ndirection == 3:
    toi = nsqx * sqlen - 1
    if nsame:
      toj = (nsqy - 1) * sqlen + coord
    else:
      toj = nsqy * sqlen - 1 - coord

  return toi, toj, ndirection

def wrap_cube_sample():
  return {
    0: {
      0: (11, 15, 2),
      1: (10, 15, 2),
      2: (9, 15, 2),
      3: (8, 15, 2),

      4: (8, 15, 1),
      5: (8, 14, 1),
      6: (8, 13, 1),
      7: (8, 12, 1),

      8: (3, 15, 2),
      9: (2, 15, 2),
      10: (1, 15, 2),
      11: (0, 15, 2)
    },
    1: {
      0: (11, 11, 3),
      1: (11, 10, 3),
      2: (11, 9, 3),
      3: (11, 8, 3),

      4: (11, 8, 0),
      5: (10, 8, 0),
      6: (9, 8, 0),
      7: (8, 8, 0),

      8: (7, 3, 3),
      9: (7, 2, 3),
      10: (7, 1, 3),
      11: (7, 0, 3),

      12: (7, 15, 0),
      13: (7, 14, 0),
      14: (7, 13, 0),
      15: (7, 12, 0)
    },
    2: {
      0: (4, 4, 1),
      1: (4, 5, 1),
      2: (4, 6, 1),
      3: (4, 7, 1),

      4: (11, 15, 3),
      5: (11, 14, 3),
      6: (11, 13, 3),
      7: (11, 12, 3),

      8: (7, 7, 3),
      9: (7, 6, 3),
      10: (7, 5, 3),
      11: (7, 4, 3)
    },
    3: {
      0: (0, 11, 1),
      1: (0, 10, 1),
      2: (0, 9, 1),
      3: (0, 8, 1),

      4: (0, 8, 0),
      5: (1, 8, 0),
      6: (2, 8, 0),
      7: (3, 8, 0),

      8: (4, 3, 1),
      9: (4, 2, 1),
      10: (4, 1, 1),
      11: (4, 0, 1),

      12: (11, 11, 2),
      13: (10, 11, 2),
      14: (9, 11, 2),
      15: (8, 11, 2)
    }
  }

def paround(board, x, y):
  for i in range(x - 1, min(len(board), x + 2)):
    print(board[x][y-1:min(len(board), y + 2)])

def pfull(board, x, y, direction):
  nboard = [[' ' if s == '.' else s for s in row] for row in board]
  nboard[x][y] = ['>', 'v', '<', '^'][direction]

  for i in range(len(nboard)):
    print(''.join(nboard[i]))

  print()

main()

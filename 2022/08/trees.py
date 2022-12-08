def main():
  data = read_file_to_list()

  process(data)
  visibles, view = process(data)
  print(visibles)
  print(view)

def read_file_to_list():
  with open('input.txt') as f:
    content = f.read().splitlines()

  return content

def process(data):
  # part 1
  visibles = 0

  for i in range(len(data)):
    for j in range(len(data[i])):
      current = data[i][j]

      if i == 0 or j == 0 or i == len(data) - 1 or j == len(data[i]) - 1:
        visibles += 1
        continue

      # left
      k  = i
      sl = 0
      for l in range(j):
        sl += 1
        if current <= data[k][l]:
          break
      else:
        visibles += 1
        continue

      # right
      k  = i
      sr = 0
      for l in range(j + 1, len(data[i])):
        sr += 1
        if current <= data[k][l]:
          break
      else:
        visibles += 1
        continue

      # up
      l  = j
      su = 0
      for k in range(i):
        su += 1
        if current <= data[k][l]:
          break
      else:
        visibles += 1
        continue

      # down
      l  = j
      sd = 0
      for k in range(i + 1, len(data)):
        sd += 1
        if current <= data[k][l]:
          break
      else:
        visibles += 1
        continue

  # part 2
  best_score = 0
  best_tree  = None

  for i in range(len(data)):
    for j in range(len(data[i])):
      current = data[i][j]

      # left
      k  = i
      sl = 0
      for l in range(j - 1, -1, -1):
        sl += 1
        if current <= data[k][l]:
          break

      # right
      k  = i
      sr = 0
      for l in range(j + 1, len(data[i])):
        sr += 1
        if current <= data[k][l]:
          break

      # up
      l  = j
      su = 0
      for k in range(i - 1, -1, -1):
        su += 1
        if current <= data[k][l]:
          break

      # down
      l  = j
      sd = 0
      for k in range(i + 1, len(data)):
        sd += 1
        if current <= data[k][l]:
          break

      score = sl * sr * su * sd
      if best_score < score:
        best_score = score
        best_tree  = i, j

  return visibles, best_score

main()

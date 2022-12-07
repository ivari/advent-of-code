def main():
  data   = read_file_to_list()

  total, smallest = process(data)
  print(total)
  print(smallest)

def read_file_to_list():
  with open('history.txt') as f:
    content = f.read().splitlines()

  return content

def process(data):
  current = []
  sizes   = {}

  # part one

  for line in data:
    if line[0:4] == '$ cd':
      if line[5:] == '/':
        current = []
      elif line[5:] == '..':
        current.pop()
      else:
        current.append(line[5:])

    elif line[0:3] == 'dir':
      pass

    elif line[0:4] == '$ ls':
      pass

    else:
      bits = line.split(' ')

      for i in range(len(current), -1, -1):
        path = '/'.join(current[0:i])

        if not path in sizes:
          sizes[path] = 0

        sizes[path] += int(bits[0])

  total = 0
  for a in sizes:
    if sizes[a] <= 100000:
      total += sizes[a]

  # part two

  freespace = 70000000 - sizes['']
  missing   = 30000000 - freespace
  smallest  = None
  for a in sizes:
    if sizes[a] >= missing:
      if smallest == None or sizes[a] < sizes[smallest]:
        smallest = a

  return total, sizes[smallest]

main()

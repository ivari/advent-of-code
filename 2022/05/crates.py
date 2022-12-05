def main():
  instructions = read_file_to_list()

  for machine in [9000, 9001]:
    stacks = process_crates(instructions, machine == 9001)

    for s in stacks:
      print(s[-1:][0], end='')
    print()

def read_file_to_list():
  with open('stacks.txt') as f:
    content = f.read().splitlines()

  return content

def process_crates(lines, is_9001=False):
  stacks  = []

  split   = 0
  current = 0
  for i in range(len(lines)):
    if lines[i] == '':
      split = i
      break

  current = split - 2
  for i in range(current, -1, -1):
    line = lines[i]

    s = 0
    for j in range(1, len(line), 4):
      crate = line[j]
      # print(line[j:j+1])

      if len(stacks) <= s:
        stacks.append([])

      if crate != ' ':
        stacks[s].append(crate)

      s += 1

  current = split + 1
  for i in range(current, len(lines)):
    words = lines[i].split(' ')

    count = int(words[1])
    mfrom = int(words[3]) - 1
    mto   = int(words[5]) - 1

    if is_9001:
      memory = []
      for j in range(count):
        if 0 < len(stacks[mfrom]):
          crate = stacks[mfrom].pop()
          memory.append(crate)

      for j in range(count):
        crate = memory.pop()
        stacks[mto].append(crate)

    else:
      for j in range(count):
        if 0 < len(stacks[mfrom]):
          crate = stacks[mfrom].pop()
          stacks[mto].append(crate)

  return stacks

main()

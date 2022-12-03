def main():
  elves = read_file_to_list()

  best_fed = find_best_fed_elf(elves)
  print(best_fed)

  three_best_fed = find_three_best_fed_elf(elves)
  print(three_best_fed)

def read_file_to_list():
  with open('calories.txt') as f:
    content = f.read().splitlines()

  elves = [0]
  for line in content:
    if line == '':
      elves.append(0)
      continue

    elves[len(elves) - 1] += int(line)

  return elves

def find_best_fed_elf(elves):
  return max(elves)

def find_three_best_fed_elf(elves):
  return sum(sorted(elves)[-3:])

main()

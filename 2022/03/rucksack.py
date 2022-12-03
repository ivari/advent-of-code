def main():
  sacks = read_file_to_list()

  total, total_in_groups = process_rucksacks(sacks)
  print(total)
  print(total_in_groups)

def read_file_to_list():
  with open('rucksacks.txt') as f:
    content = f.read().splitlines()

  return content

def process_rucksacks(sacks):
  priorities = 0
  priorities_in_groups = 0

  for sack in sacks:
    items    = len(sack) // 2
    section1 = sack[:items]
    section2 = sack[items:]

    common = [x for x in section1 if x in section2][0]

    priorities += priority(common)

  for i in range(0, len(sacks), 3):
    group = sacks[i:i+3]

    common = [x for x in group[0] if x in group[1] if x in group[2]][0]

    priorities_in_groups += priority(common)

  return priorities, priorities_in_groups

def priority(item):
  if ord(item) < ord('a'):
    return ord(item) - 64 + 26

  return ord(item) - 96

main()

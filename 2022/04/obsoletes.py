def main():
  pairs = read_file_to_list()

  contains, overlaps = verify_pairs(pairs)
  print(contains)
  print(overlaps)

def read_file_to_list():
  with open('assignments.txt') as f:
    content = f.read().splitlines()

  return content

def verify_pairs(pairs):
  contains = 0
  overlaps = 0

  for assigned in pairs:
    pair   = assigned.split(',')

    first  = pair[0].split('-')
    second = pair[1].split('-')

    start1 = int(first[0])
    end1   = int(first[1])

    start2 = int(second[0])
    end2   = int(second[1])

    if start1 <= start2 and end1 >= end2 or start2 <= start1 and end2 >= end1:
      contains += 1

    if 0 < len([x for x in range(start1, end1 + 1) if x in range(start2, end2 + 1)]):
      overlaps += 1

  return contains, overlaps

main()

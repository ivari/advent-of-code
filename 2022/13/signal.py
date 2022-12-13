import functools

def main():
  data     = read_file_to_list()

  indices  = verify(data)
  dividers = order(data)

  print('Sum of indices for correct pairs:',    indices)
  print('Sum of indices for divider packages:', dividers)

def read_file_to_list():
  with open('input.txt') as f:
    content = f.read().splitlines()

  return content

def verify(data):
  current = 0
  total   = 0

  first   = None
  second  = None

  for s in data:
    if s == '':
      continue

    if first == None:
      first = s
      continue

    if second == None:
      second = s


    if first != None and second != None:
      current += 1
      first    = eval(first)
      second   = eval(second)

      result = compare(first, second)

      if result == 0:
        raise 'Unable to calculate result for index ' + str(current)

      if result < 0:
        total += current

    first  = None
    second = None

  return total

def order(data):
  dividers = [[[2]], [[6]]]
  packets  = list(dividers)
  total    = 1

  for s in data:
    if s == '':
      continue

    packets.append(eval(s))

  spackets = sorted(packets, key = functools.cmp_to_key(compare))

  for i in range(len(spackets)):
    if spackets[i] in dividers:
      total *= i + 1

  return total

# Returns -1 for right order, 1 for wrong order
def compare(left, right):
  if isinstance(left, int) and isinstance(right, int):
    if left == right:
      return 0

    return -1 if left < right else 1

  if isinstance(left, int):
    return compare([left], right)

  if isinstance(right, int):
    return compare(left, [right])

  for i in range(max(len(left), len(right))):
    if len(left) <= i:
      return -1

    if len(right) <= i:
      return 1

    result = compare(left[i], right[i])
    if result != 0:
      return -1 if result < 0 else 1

  return 0

main()

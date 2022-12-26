with open('input.txt') as f:
  input_lines = f.read().splitlines()

def unsnafu(base5):
  base10 = 0
  for i in range(len(base5) - 1, -1, -1):
    power = abs(i + 1 - len(base5))

    if base5[i] in ['0', '1', '2']:
      current = base5[i]
    elif base5[i] == '-':
      current = -1
    elif base5[i] == '=':
      current = -2
    else:
      raise Exception('Unknown digit found in ' + base5)

    base10 += int(current) * (5 ** power)

  return base10

nums = []
for base5 in input_lines:
  print(base5, unsnafu(base5))
  nums.append(unsnafu(base5))

print()

total = sum(nums)
print('Total:', total)

def snafufy(total, result = ''):
  remainder = total % 5
  digit = str(remainder)

  total -= remainder

  if remainder == 4:
    digit = '-'
    total += 5

  elif remainder == 3:
    digit = '='
    total += 5

  result = digit + result
  if total == 0:
    return result

  return snafufy(total // 5, result)

print('Result:', snafufy(total))

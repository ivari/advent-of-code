def main():
  data = read_file_to_list()

  with_relief    = process(data, 20)
  print(with_relief)

  without_relief = process(data, 10000, False)
  print(without_relief)

def read_file_to_list():
  with open('input.txt') as f:
    content = f.read().splitlines()

  return content

def process(data, rounds, relief = True):
  primes  = set()
  monkeys = []

  monkey  = None
  for i in range(len(data)):
    line = data[i]

    if line[0:6] == 'Monkey':
      if monkey != None:
        monkeys.append(monkey)

      monkey = {}

    elif line[2:10] == 'Starting':
      monkey['items'] = []
      for item in line[18:].split(', '):
        monkey['items'].append([factors(int(item)), 0])

    elif line[2:11] == 'Operation':
      monkey['operation'] = line[19:]

    elif line[2:6] == 'Test':
      monkey['test'] = int(line[21:])
      primes.add(monkey['test'])

    elif line[7:11] == 'true':
      monkey['true'] = int(line[29:])

    elif line[7:12] == 'false':
      monkey['false'] = int(line[30:])

  monkeys.append(monkey)
  inspects       = [0] * len(monkeys)

  min_product    = 1
  for x in primes:
    min_product *= x

  for r in range(rounds):
    if r % 20 == 0:
      print('Progress:', int(r / rounds * 100), '%', 'done')

    for m in range(len(monkeys)):
      monkey = monkeys[m]
      items  = monkey['items']
      monkeys[m]['items'] = []

      for item in items:
        worry = item

        inspects[m] += 1

        # inspect

        bits = monkey['operation'].split(' ')
        if bits[1] == '+' and bits[2] == 'old':
          bits[1] = '*'
          bits[2] = '2'

        worry     = product(worry[0]) + worry[1]

        if bits[1] == '+':
          worry  += int(bits[2])

        elif bits[1] == '*' and bits[2] == 'old':
          worry   = worry ** 2

        elif bits[1] == '*':
          worry  *= int(bits[2])

        else:
          raise 'Error: operation type missed'

        # relief

        if relief:
          worry = worry // 3

        # optimize

        while min_product < worry:
          worry -= min_product
        worry = [list(primes), worry - min_product]

        # throw

        test  = monkey['test']
        in_fs = test in worry[0]
        cond  = in_fs and worry[1] == 0
        cond  = cond or (in_fs and worry[1] % test == 0)
        cond  = cond or (product(worry[0]) + worry[1]) % test == 0

        recip = 'true' if cond else 'false'
        monkeys[monkey[recip]]['items'].append(worry)

  print('Progress:', 100, '%', 'done')

  result = sorted(inspects)

  return result[-2] * result[-1]

def factors(n):
  result = []

  while 1 < n:
    for x in range(2, int(n ** 0.5) + 2):
      if n % x == 0:
        result.append(x)
        n = n // x
    else:
      result.append(n)
      break

  return result

def product(factors):
  result  = 1

  for x in factors:
    result *= x

  return result

main()

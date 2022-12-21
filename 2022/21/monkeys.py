with open('input.txt') as f:
  input_lines = f.read().splitlines()

monkeys = {}

for line in input_lines:
  data = line.split(':')

  if '+' in data[1] or '-' in data[1] or '*' in data[1] or '/' in data[1]:
    bits = data[1].split(' ')
    monkeys[data[0]] = bits[2], bits[1], bits[3]

  else:
    monkeys[data[0]] = int(data[1])

def resolve(name, humn = False):
  global monkeys

  math = monkeys[name]

  if isinstance(math, int):
    if humn and name == 'humn':
      return name

    return math

  if isinstance(math, tuple):
    left  = resolve(math[1], humn)
    right = resolve(math[2], humn)

    if humn and name == 'root':
      return print_math(left), print_math(right)

    if isinstance(left, str) or isinstance(right, str) \
      or isinstance(left, tuple) or isinstance(right, tuple):
      return math[0], left, right

    if math[0] == '+':
      return left + right

    if math[0] == '-':
      return left - right

    if math[0] == '*':
      return left * right

    if math[0] == '/':
      return left // right

  raise Exception('Unknown monkey data: ' + str(math))

def print_math(value):
  if isinstance(value, tuple):
    return '(%s %s %s)' % (
      print_math(value[1]),
      value[0],
      print_math(value[2])
    )

  return str(value)

p1 = resolve('root')
print('Part 1:', p1)

p2 = resolve('root', True)
print('Part 2:', p2[0], '=', p2[1]) # then solve for x

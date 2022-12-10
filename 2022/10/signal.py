def main():
  data = read_file_to_list()

  total, display = process(data)

  print(total)
  print(display)

def read_file_to_list():
  with open('input.txt') as f:
    content = f.read().splitlines()

  return content

def process(data):
  strength = {
     20: None,
     60: None,
    100: None,
    140: None,
    180: None,
    220: None
  }

  horizontal = 40
  vertical   = 6
  pixels     = ['.'] * horizontal * vertical

  current = 1
  cycle   = 0
  for instr in data:
    command = instr[0:4]

    if command == 'noop':
      cycle += 1

    elif command == 'addx':
      cycle += 1
      pixels = draw_pixel(pixels, current, cycle)

      cycle += 1

    for n in strength:
      if n <= cycle and strength[n] == None:
        strength[n] = n * current

    pixels = draw_pixel(pixels, current, cycle)

    if command == 'addx':
      current += int(instr[5:])

  total = 0
  for n in strength:
    if strength[n] != None:
      total += strength[n]

  return total, print_display(pixels, horizontal)

def draw_pixel(pixels, current, cycle):
  position = cycle - 1
  row      = position // 40
  sprite   = (row * 40) + current - 1

  if sprite <= position and position <= sprite + 2:
    pixels[position] = '#'

  return pixels

def print_display(pixels, horizontal):
  display = ''
  for i in range(0, len(pixels), horizontal):
    display += ''.join(pixels[i:i+40])
    display += '\n'

  return display

main()

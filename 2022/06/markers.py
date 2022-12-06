def main():
  data = read_file_to_list()

  ma   = marker(data)
  me   = message(data)

  print(ma)
  print(me)

def read_file_to_list():
  with open('data.txt') as f:
    content = f.read().strip()

  return content

def marker(data):
  for i in range(len(data) - 4):
    candidate = data[i:i+4]

    if len(candidate) == len(set(candidate)):
      return i + 4

def message(data):
  for i in range(len(data) - 14):
    candidate = data[i:i+14]

    if len(candidate) == len(set(candidate)):
      return i + 14

main()

POINTS = {
  'X'   : 1,
  'Y'   : 2,
  'Z'   : 3,
  'loss': 0,
  'tie' : 3,
  'win' : 6
}

GAMES = {
  'losses': ['A Z', 'B X', 'C Y'],
  'ties'  : ['A X', 'B Y', 'C Z'],
  'wins'  : ['A Y', 'B Z', 'C X']
}

def main():
  rounds = read_file_to_list()

  total = 0
  for round in rounds:
    total += points_for_round(round)

  print(total)

  correct_total = 0
  for round in rounds:
    correct_total += points_for_round(round, True)

  print(correct_total)

def read_file_to_list():
  with open('guide.txt') as f:
    content = f.read().splitlines()

  return content

def points_for_round(round, correct_instructions = False):
  if correct_instructions:
    points = 0

    if round[2] == 'X':
      points += POINTS['loss'] + POINTS[losing_move(round[0])]

    if round[2] == 'Y':
      points += POINTS['tie'] + POINTS[tieing_move(round[0])]

    if round[2] == 'Z':
      points += POINTS['win'] + POINTS[winning_move(round[0])]

  else:
    points = POINTS[round[2]]

    if round in GAMES['losses']:
      points += POINTS['loss']

    if round in GAMES['ties']:
      points += POINTS['tie']

    if round in GAMES['wins']:
      points += POINTS['win']

  return points

def losing_move(opponent):
  if opponent == 'A':
    return 'Z'

  if opponent == 'B':
    return 'X'

  if opponent == 'C':
    return 'Y'

def tieing_move(opponent):
  if opponent == 'A':
    return 'X'

  if opponent == 'B':
    return 'Y'

  if opponent == 'C':
    return 'Z'

def winning_move(opponent):
  if opponent == 'A':
    return 'Y'

  if opponent == 'B':
    return 'Z'

  if opponent == 'C':
    return 'X'

main()

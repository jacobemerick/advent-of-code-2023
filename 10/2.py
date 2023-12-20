import sys
sys.setrecursionlimit(9999)

field = []
startingLocation = []

file = open('input.txt', 'r')
for line in file:
  field.append([*line.strip()])
  if 'S' in field[-1]:
    currentLocation = [len(field) - 1, field[-1].index('S')]
file.close()

previousLocation = currentLocation
if currentLocation[0] > 0 and field[currentLocation[0] - 1][currentLocation[1]] in ['|', '7', 'F']:
  currentLocation = [currentLocation[0] - 1, currentLocation[1]]
if currentLocation[1] < len(field[currentLocation[0]]) - 1 and field[currentLocation[0]][currentLocation[1] + 1] in ['-', '7', 'J']:
  currentLocation = [currentLocation[0], currentLocation[1] + 1]
if currentLocation[0] < len(field) - 1 and field[currentLocation[0] + 1][currentLocation[1]] in ['|', 'J', 'L']:
  currentLocation = [currentLocation[0] + 1, currentLocation[1]]
if currentLocation[1] > 0 and field[currentLocation[0]][currentLocation[1] - 1] in ['-', 'L', 'F']:
  currentLocation = [currentLocation[0], currentLocation[1] - 1]

while field[currentLocation[0]][currentLocation[1]] != 'x':
  field[previousLocation[0]][previousLocation[1]] = 'x'
  if field[currentLocation[0]][currentLocation[1]] == 'F':
    if previousLocation[0] - 1 == currentLocation[0]:
      previousLocation = currentLocation
      currentLocation = [currentLocation[0], currentLocation[1] + 1]
    else:
      previousLocation = currentLocation
      currentLocation = [currentLocation[0] + 1, currentLocation[1]]
    continue

  if field[currentLocation[0]][currentLocation[1]] == '7':
    if previousLocation[0] - 1 == currentLocation[0]:
      previousLocation = currentLocation
      currentLocation = [currentLocation[0], currentLocation[1] - 1]
    else:
      previousLocation = currentLocation
      currentLocation = [currentLocation[0] + 1, currentLocation[1]]
    continue

  if field[currentLocation[0]][currentLocation[1]] == 'J':
    if previousLocation[0] + 1 == currentLocation[0]:
      previousLocation = currentLocation
      currentLocation = [currentLocation[0], currentLocation[1] - 1]
    else:
      previousLocation = currentLocation
      currentLocation = [currentLocation[0] - 1, currentLocation[1]]
    continue

  if field[currentLocation[0]][currentLocation[1]] == 'L':
    if previousLocation[0] + 1 == currentLocation[0]:
      previousLocation = currentLocation
      currentLocation = [currentLocation[0], currentLocation[1] + 1]
    else:
      previousLocation = currentLocation
      currentLocation = [currentLocation[0] - 1, currentLocation[1]]
    continue

  if field[currentLocation[0]][currentLocation[1]] == '|':
    if previousLocation[0] - 1 == currentLocation[0]:
      previousLocation = currentLocation
      currentLocation = [currentLocation[0] - 1, currentLocation[1]]
    else:
      previousLocation = currentLocation
      currentLocation = [currentLocation[0] + 1, currentLocation[1]]
    continue

  if field[currentLocation[0]][currentLocation[1]] == '-':
    if previousLocation[1] - 1 == currentLocation[1]:
      previousLocation = currentLocation
      currentLocation = [currentLocation[0], currentLocation[1] - 1]
    else:
      previousLocation = currentLocation
      currentLocation = [currentLocation[0], currentLocation[1] + 1]
    continue
  
field[previousLocation[0]][previousLocation[1]] = 'x'

def lookAround(y, x):
  if field[y][x] == 'x' or field[y][x] == ' ':
    return
  
  field[y][x] = ' '

  if y > 0:
    lookAround(y - 1, x)
  if y < len(field) - 1:
    lookAround(y + 1, x)
  if x > 0:
    lookAround(y, x - 1)
  if x < len(field[y]) - 1:
    lookAround(y, x + 1)

for y, row in enumerate(field):
  lookAround(y, 0)
  lookAround(y, len(field[y]) - 1)

for x, char in enumerate(field[0]):
  lookAround(0, x)
  lookAround(len(field) - 1, x)

inTheLoop = 0
for y, row in enumerate(field):
  for x, char in enumerate(row):
    if char == ' ' or char == 'x':
      continue
    inTheLoop += 1

print('Area in the loop', inTheLoop)
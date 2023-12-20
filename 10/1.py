field = []
startingLocation = []

file = open('input.txt', 'r')
for line in file:
  field.append([*line.strip()])
  if 'S' in field[-1]:
    currentLocation = [len(field) - 1, field[-1].index('S')]
file.close()

previousLocation = currentLocation
loopLength = 1
if currentLocation[0] > 0 and field[currentLocation[0] - 1][currentLocation[1]] in ['|', '7', 'F']:
  currentLocation = [currentLocation[0] - 1, currentLocation[1]]
if currentLocation[1] < len(field[currentLocation[0]]) - 1 and field[currentLocation[0]][currentLocation[1] + 1] in ['-', '7', 'J']:
  currentLocation = [currentLocation[0], currentLocation[1] + 1]
if currentLocation[0] < len(field) - 1 and field[currentLocation[0] + 1][currentLocation[1]] in ['|', 'J', 'L']:
  currentLocation = [currentLocation[0] + 1, currentLocation[1]]
if currentLocation[1] > 0 and field[currentLocation[0]][currentLocation[1] - 1] in ['-', 'L', 'F']:
  currentLocation = [currentLocation[0], currentLocation[1] - 1]

while field[currentLocation[0]][currentLocation[1]] != 'S':
  loopLength += 1

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
  

print('Furthest away:', int(loopLength / 2))
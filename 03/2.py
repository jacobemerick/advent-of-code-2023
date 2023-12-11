engine = []
partStore = []

file = open('input.txt', 'r')
for line in file:
  engineRow = []
  partAccumulator = ''
  characters = [*line.strip()]

  for character in characters:
    if character.isnumeric():
      partAccumulator += character
      engineRow.append(len(partStore))
    else:
      if partAccumulator != '':
        partStore.append(int(partAccumulator))
        partAccumulator = ''
      engineRow.append(character)
  
  if partAccumulator != '':
    partStore.append(int(partAccumulator))
    partAccumulator = ''

  engine.append(engineRow)
file.close()

def findNearbyParts(x, y):
  nearbyParts = set()

  if y > 0 and x > 0 and isinstance(engine[y - 1][x - 1], int):
    nearbyParts.add(engine[y - 1][x - 1])
  if y > 0 and isinstance(engine[y - 1][x], int):
    nearbyParts.add(engine[y - 1][x])
  if y > 0 and x < (len(engine[y]) - 1) and isinstance(engine[y - 1][x + 1], int):
    nearbyParts.add(engine[y - 1][x + 1])
  
  if x > 0 and isinstance(engine[y][x - 1], int):
    nearbyParts.add(engine[y][x - 1])
  if x < (len(engine[y]) - 1) and isinstance(engine[y][x + 1], int):
    nearbyParts.add(engine[y][x + 1])

  if y < (len(engine) - 1) and x > 0 and isinstance(engine[y + 1][x - 1], int):
    nearbyParts.add(engine[y + 1][x - 1])
  if y < (len(engine) - 1) and isinstance(engine[y + 1][x], int):
    nearbyParts.add(engine[y + 1][x])
  if y < (len(engine) - 1) and x < (len(engine[y]) - 1) and isinstance(engine[y + 1][x + 1], int):
    nearbyParts.add(engine[y + 1][x + 1])
  
  if len(nearbyParts) != 2:
    return False
  
  return partStore[list(nearbyParts)[0]] * partStore[list(nearbyParts)[1]]

gearRatioSum = 0
for y, row in enumerate(engine):
  for x, val in enumerate(row):
    if val != '*':
      continue
    
    hasNearbyParts = findNearbyParts(x, y)
    if hasNearbyParts != False:
      gearRatioSum += hasNearbyParts

print('Sum of all gear ratios', gearRatioSum)
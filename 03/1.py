def isSymbol(val):
  if isinstance(val, int):
    return False
  if val == '.':
    return False
  return True

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

def nearSymbol(x, y):
  if y > 0 and x > 0 and isSymbol(engine[y - 1][x - 1]):
    return True
  if y > 0 and isSymbol(engine[y - 1][x]):
    return True
  if y > 0 and x < (len(engine[y]) - 1) and isSymbol(engine[y - 1][x + 1]):
    return True
  
  if x > 0 and isSymbol(engine[y][x - 1]):
    return True
  if x < (len(engine[y]) - 1) and isSymbol(engine[y][x + 1]):
    return True

  if y < (len(engine) - 1) and x > 0 and isSymbol(engine[y + 1][x - 1]):
    return True
  if y < (len(engine) - 1) and isSymbol(engine[y + 1][x]):
    return True
  if y < (len(engine) - 1) and x < (len(engine[y]) - 1) and isSymbol(engine[y + 1][x + 1]):
    return True
  
  return False

schematicParts = set()
for y, row in enumerate(engine):
  for x, val in enumerate(row):
    if isinstance(val, str):
      continue
    
    if nearSymbol(x, y):
      schematicParts.add(val)

schematicPartSum = 0
for schematicPart in schematicParts:
  schematicPartSum += partStore[schematicPart]

print('Sum of all engine parts', schematicPartSum)
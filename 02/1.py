possibleGameIdSum = 0

def getGameId(line):
  return (int) (line.split(':')[0].split(' ')[1])

def getGameResults(line):
  gameResults = line.split(':')[1].split(';')
  return map(lambda x: x.strip(), gameResults)

def isGamePossible(game):
  cubeSubsets = map(lambda x: x.strip(), game.split(','))

  for cubeSubset in cubeSubsets:
    cubeResult = cubeSubset.split(' ')
    if cubeResult[1] == 'red' and (int) (cubeResult[0]) > 12:
      return False
    if cubeResult[1] == 'green' and (int) (cubeResult[0]) > 13:
      return False
    if cubeResult[1] == 'blue' and (int) (cubeResult[0]) > 14:
      return False
  
  return True

file = open('input.txt', 'r')
for line in file:
  gameId = getGameId(line)
  gameResults = getGameResults(line)

  possibleGame = True
  for gameResult in gameResults:
    if isGamePossible(gameResult) == False:
      possibleGame = False
      break

  if possibleGame:
    possibleGameIdSum += gameId

file.close()
print('Sum of all possible game ids', possibleGameIdSum)
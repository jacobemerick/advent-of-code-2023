sumOfAllGamePowers = 0

def getGamePower(line):
  red = 0
  green = 0
  blue = 0

  roundResults = map(lambda x: x.strip(), line.split(':')[1].split(';'))
  for roundResult in roundResults:
    cubeSubsets = map(lambda x: x.strip(), roundResult.split(','))
    for cubeSubset in cubeSubsets:
      cubeResult = cubeSubset.split(' ')
      if cubeResult[1] == 'red' and (int) (cubeResult[0]) > red:
        red = (int) (cubeResult[0])
      if cubeResult[1] == 'green' and (int) (cubeResult[0]) > green:
        green = (int) (cubeResult[0])
      if cubeResult[1] == 'blue' and (int) (cubeResult[0]) > blue:
        blue = (int) (cubeResult[0])
  
  return red * green * blue

file = open('input.txt', 'r')
for line in file:
  sumOfAllGamePowers += getGamePower(line)

file.close()
print('Sum of all game powers', sumOfAllGamePowers)
timeRecords = []
distanceRecords = []

file = open('input.txt', 'r')
for line in file:
  parsedLine = line.strip().split(':')
  values = list(map(lambda x: int(x), list(filter(lambda x: x != '', parsedLine[1].split(' ')))))

  if parsedLine[0] == 'Time':
    timeRecords = values
  if parsedLine[0] == 'Distance':
    distanceRecords = values
file.close()

multipledWinningOptions = 1
for raceNumber, raceTime in enumerate(timeRecords):
  buttonPress = 0
  buttonPressWins = 0
  while buttonPress <= raceTime:
    distance = buttonPress * (raceTime - buttonPress)
    if distance > distanceRecords[raceNumber]:
      buttonPressWins += 1
    buttonPress += 1
  
  multipledWinningOptions *= buttonPressWins

print('Multipled winning options:', multipledWinningOptions)
    

raceTime = 0
raceDistance = 0

file = open('input.txt', 'r')
for line in file:
  parsedLine = line.strip().split(':')
  values = int(''.join(list(filter(lambda x: x != '', parsedLine[1].split(' ')))))

  if parsedLine[0] == 'Time':
    raceTime = values
  if parsedLine[0] == 'Distance':
    raceDistance = values
file.close()

buttonPress = 0
buttonPressWins = 0
while buttonPress <= raceTime:
  distance = buttonPress * (raceTime - buttonPress)
  if distance > raceDistance:
    buttonPressWins += 1
  buttonPress += 1

print('Winning options:', buttonPressWins)
    

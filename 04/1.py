totalPoints = 0

file = open('input.txt', 'r')
for line in file:
  parsedLine = line.strip().split(':')[1].split('|')
  winningNumbers = list(filter(None, parsedLine[0].split(' ')))
  cardNumbers = list(filter(None, parsedLine[1].split(' ')))

  matchingNumbers = 0
  for cardNumber in cardNumbers:
    if cardNumber in winningNumbers:
      matchingNumbers += 1
  
  if matchingNumbers > 0:
    totalPoints += pow(2, matchingNumbers - 1)
file.close()

print('Total points won', totalPoints)
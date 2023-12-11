cardList = []
cardCount = []

file = open('input.txt', 'r')
for line in file:
  parsedLine = line.strip().split(':')[1].split('|')
  winningNumbers = list(filter(None, parsedLine[0].split(' ')))
  cardNumbers = list(filter(None, parsedLine[1].split(' ')))

  matchingNumbers = 0
  for cardNumber in cardNumbers:
    if cardNumber in winningNumbers:
      matchingNumbers += 1
  
  cardList.append(matchingNumbers)
  cardCount.append(1)
file.close()

for i, cardWinnings in enumerate(cardList):
  copyCount = cardCount[i]

  j = 0
  while j < cardWinnings:
    j += 1
    cardCount[i + j] += copyCount

print('Total number of cards:', sum(cardCount))
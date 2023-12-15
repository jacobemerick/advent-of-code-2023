from functools import cmp_to_key, reduce
import itertools

def getHandTypeStrength(hand):
  sortedHand = sorted([*hand])
  groupedHands = []
  for i, group in itertools.groupby(sortedHand):
    groupedHands.append(list(group))
  sortedGroups = sorted(groupedHands, key=lambda x: len(x), reverse=True)

  if (len(sortedGroups[0]) == 5):
    return 0
  if (len(sortedGroups[0]) == 4):
    return 1
  if (len(sortedGroups[0]) == 3 and len(sortedGroups[1]) == 2):
    return 2
  if (len(sortedGroups[0]) == 3):
    return 3
  if (len(sortedGroups[0]) == 2 and len(sortedGroups[1]) == 2):
    return 4
  if (len(sortedGroups[0]) == 2):
    return 5
  return 6

cardStrength = ['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2']
def getHandStrength(hand, index):
  return cardStrength.index([*hand][index])

def compareTypes(hand1, hand2):
  if getHandTypeStrength(hand1[0]) == getHandTypeStrength(hand2[0]):
    for i in range(5):
      if getHandStrength(hand1[0], i) == getHandStrength(hand2[0], i):
        continue
      return getHandStrength(hand1[0], i) - getHandStrength(hand2[0], i)
    raise Exception('complete tie')
  return getHandTypeStrength(hand1[0]) - getHandTypeStrength(hand2[0])

hands = []
file = open('input.txt', 'r')
for line in file:
  hands.append(line.strip().split(' '))
file.close()

hands = sorted(hands, key=cmp_to_key(compareTypes), reverse=True)

totalWinnings = 0
for index, hand in enumerate(hands):
  totalWinnings += int(hand[1]) * (index + 1)
print('Total winnings', totalWinnings)
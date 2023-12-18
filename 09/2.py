predictedValues = []

def hasNonZeroValue(values):
  for value in values:
    if value != 0:
      return True
  return False

def calculateStepDifferences(values):
  stepDifferences = []
  for i in range(len(values) - 1):
    stepDifferences.append(values[i + 1] - values[i])
  return stepDifferences

file = open('input.txt', 'r')
for line in file:
  values = list(map(int, line.strip().split(' ')))

  differences = []
  differences.append(values)

  while hasNonZeroValue(differences[-1]):
    differences.append(calculateStepDifferences(differences[-1]))

  for i in range(len(differences) - 1, -1, -1):
    if i == len(differences) - 1:
      differences[i].insert(0, 0)
      continue
    differences[i].insert(0, differences[i][0] - differences[i + 1][0])

  predictedValues.append(differences[0][0])
file.close()

print('Sum of predicted values', sum(predictedValues))
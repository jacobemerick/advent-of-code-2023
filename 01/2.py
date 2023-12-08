calibrationValueSum = 0
englishNumbers = {
  'one': '1',
  'two': '2',
  'three': '3',
  'four': '4',
  'five': '5',
  'six': '6',
  'seven': '7',
  'eight': '8',
  'nine': '9',
}

def isPartialMatch(accumulatedNumber):
  for englishNumber in englishNumbers:
    if englishNumber.startswith(accumulatedNumber):
      return True
  return False

file = open('input.txt', 'r')
for line in file:
  firstDigit = False
  lastDigit = False
  accumulatedNumber = ''
  charList = [*line.strip()]

  for char in charList:
    if char.isnumeric():
      if firstDigit == False:
        firstDigit = char
        lastDigit = char
      else:
        lastDigit = char
      continue
    
    accumulatedNumber += char
    if accumulatedNumber in englishNumbers:
      if firstDigit == False:
        firstDigit = englishNumbers[accumulatedNumber]
        lastDigit = englishNumbers[accumulatedNumber]
      else:
        lastDigit = englishNumbers[accumulatedNumber]
      continue
    
    while isPartialMatch(accumulatedNumber) == False and len(accumulatedNumber) > 0:
      accumulatedNumber = accumulatedNumber[1:]
  
  calibrationValue = (int) (firstDigit + lastDigit)
  calibrationValueSum += calibrationValue

file.close()
print('Sum of all fears', calibrationValueSum)
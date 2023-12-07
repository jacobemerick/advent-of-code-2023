calibrationValueSum = 0

file = open('input.txt', 'r')
for line in file:
  firstDigit = False
  lastDigit = False
  charList = [*line.strip()]

  for char in charList:
    if char.isnumeric():
      if firstDigit == False:
        firstDigit = char
        lastDigit = char
      else:
        lastDigit = char
  
  calibrationValue = (int) (firstDigit + lastDigit)
  calibrationValueSum += calibrationValue

file.close()
print('Sum of all fears', calibrationValueSum)
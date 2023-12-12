seedList = []
seedToSoilMap = []
soilToFertilizerMap = []
fertilizerToWaterMap = []
waterToLightMap = []
lightToTemperatureMap = []
temperatureToHumidityMap = []
humidityToLocationMap = []

currentMap = ''
file = open('input.txt', 'r')
for line in file:
  line = line.strip()

  if currentMap == '':
    parsedLine = line.split(':')
    if parsedLine[0] == 'seeds':
      seedList = list(map(int, parsedLine[1].strip().split(' ')))
    else:
      currentMap = parsedLine[0].split(' ')[0]
    continue
  
  if line == '':
    currentMap = ''
    continue
  
  if currentMap == 'seed-to-soil':
    seedToSoilMap.append((list(map(int, line.split(' ')))))
  if currentMap == 'soil-to-fertilizer':
    soilToFertilizerMap.append((list(map(int, line.split(' ')))))
  if currentMap == 'fertilizer-to-water':
    fertilizerToWaterMap.append((list(map(int, line.split(' ')))))
  if currentMap == 'water-to-light':
    waterToLightMap.append((list(map(int, line.split(' ')))))
  if currentMap == 'light-to-temperature':
    lightToTemperatureMap.append((list(map(int, line.split(' ')))))
  if currentMap == 'temperature-to-humidity':
    temperatureToHumidityMap.append((list(map(int, line.split(' ')))))
  if currentMap == 'humidity-to-location':
    humidityToLocationMap.append((list(map(int, line.split(' ')))))
file.close()

def getMappedValue(source, currentMap):
  for mapping in currentMap:
    if source < mapping[1]:
      continue
    if source > (mapping[1] + mapping[2]):
      continue
    return (mapping[0] - mapping[1]) + source
  return source

def processSeed(seed):
  soil = getMappedValue(seed, seedToSoilMap)
  fertilizer = getMappedValue(soil, soilToFertilizerMap)
  water = getMappedValue(fertilizer, fertilizerToWaterMap)
  light = getMappedValue(water, waterToLightMap)
  temperature = getMappedValue(light, lightToTemperatureMap)
  humidity = getMappedValue(temperature, temperatureToHumidityMap)
  location = getMappedValue(humidity, humidityToLocationMap)
  return location

lowestLocation = float('inf')

i = 0
while i < len(seedList):
  seed = seedList[i]
  maxSeed = seedList[i] + seedList[i + 1]

  while seed <= maxSeed:
    seedLocation = processSeed(seed)
    if seedLocation < lowestLocation:
      lowestLocation = seedLocation
    seed += 1
  
  i += 2

print('Lowest location', lowestLocation)
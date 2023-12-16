from math import lcm

instructions = []
nodes = {}

file = open('input.txt', 'r')
for line in file:
  line = line.strip()
  if len(instructions) == 0:
    instructions = [*line]
  elif line == '':
    continue
  else:
    parsedLine = line.split(' = ')
    node = parsedLine[0]
    connections = parsedLine[1].replace('(', '').replace(')', '').split(', ')
    nodes.update({ node: connections })
file.close()

currentLocation = []
for node in nodes:
  if node.endswith('A'):
    currentLocation.append(node)

step = 0
solutions = []
while True:
  instruction = instructions[step % len(instructions)]
  step += 1
  newCurrentLocation = []
  for node in currentLocation:
    if instruction == 'L':
      newNode = nodes[node][0]
    if instruction == 'R':
      newNode = nodes[node][1]
    
    if newNode.endswith('Z'):
      solutions.append(step)
    else:
      newCurrentLocation.append(newNode)
  
  if len(newCurrentLocation) == 0:
    break
  
  currentLocation = newCurrentLocation


print('Steps needed for ghost to reach **Z', lcm(*solutions))
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

step = 0
currentLocation = 'AAA'
while currentLocation != 'ZZZ':
  instruction = instructions[step % len(instructions)]
  step += 1
  if instruction == 'L':
    currentLocation = nodes[currentLocation][0]
  if instruction == 'R':
    currentLocation = nodes[currentLocation][1]

print('Steps needed to reach ZZZ', step)
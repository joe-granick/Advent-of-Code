from collections import defaultdict
actions = {}

hor = 0
vert = 0
aim = 0

with open('input.txt') as f:
    lines = f.readlines()

for line in lines:
    commands = line.split()
    k = commands[0]
    v = int(commands[1])

    if k == 'forward':
        hor += v
        vert += v*aim

    if k == 'down':
        #vert += v
        aim += v

    if k == 'up':
        #vert -= v
        aim -= v
        
    #if a not in actions:
    #    actions[k] = 0 + int(v)
    #else:
    #    actions[k] = actions[k] + int(v)


print(hor*vert)
    
        
    

#class submarine(depth, horizontal):

#####--------------I'm Melting---------####
####PART 1##########################################
###############------Import data----------------####
from collections import defaultdict
with open("test_input.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()

#print(lines)
end_line = len(lines)-1
print(end_line)
end_height = len(lines[0])-1
print(end_height)
low_points = []


def actions(coordinates):
    actions = []
    if coordinates[0] > 0:
        actions.append((-1, 0))
    if coordinates[1] > 0:
        actions.append((0, -1))
    if coordinates[0]+1 < end_height:
        actions.append((1, 0))
    if coordinates[1] < end_line:
        actions.append((0, 1))
    return actions

for i in range(len(lines)):
    coord = None
    for h in range(len(lines[i])-1):
        coord = (h, i)
        moves = actions(coord)
        count = 0
        print(low_points)
        print(moves)
        print("y: ", i)
        print("x: ", h)
        for move in moves:
           # print("Vertical Move:", move[1])
            #print("Horizontal Move: ", move[0])
            if lines[i][h] < lines[i + move[1]][h + move[0]]:
                count +=1
            if count == len(moves):
                low_points.append(lines[i][h])

print(low_points)
total = 0
for i in low_points:
    total += int(i)+1
print(total)




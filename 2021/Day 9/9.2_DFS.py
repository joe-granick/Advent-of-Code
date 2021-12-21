#####--------------I'm Melting---------####
####PART 1##########################################
###############------Import data----------------####
from collections import defaultdict
from os import X_OK
with open("test_input.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()

#print(lines)
end_line = len(lines)-1
print(end_line)
end_height = len(lines[0])-1
print(end_height)
low_points = []
low_coord = []


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
       # print(low_points)
       # print(moves)
       # print("y: ", i)
        #print("x: ", h)
        for move in moves:
           # print("Vertical Move:", move[1])
            #print("Horizontal Move: ", move[0])
            if lines[i][h] < lines[i + move[1]][h + move[0]]:
                count +=1
            if count == len(moves):
                low_points.append(lines[i][h])
                low_coord.append((h, i))

print(low_points)
print(low_coord[0])
total = 0
for i in low_points:
    total += int(i)+1
print(total)

def succ(coord):
    next_coord = []
    x = coord[0] 
    y = coord[1]
    for action in actions(coord):
        if int(lines[y+ action[1]][x+action[0]]) and int(lines[y+ action[1]][x+action[0]]) < 9:
            next_coord.append((x+action[0], y+action[1]))
    return next_coord

bas = defaultdict(lambda: None)
def DFS(coord, memo = []):
    print("Searched Coordinate: ", memo)

    if len(coord) == 0:
        return memo
    
    elif coord[0] in memo:
        #bas[coord[0]] = memo[:]
        print("move: ", coord[1:])
        print(coord)
        #memo.append(coord[1])
        return DFS(coord[1:], memo)
        #return DFS(coord[1:],  memo)

    else:
        memo.append(coord[0])
        return DFS(succ(coord[0]), memo) + DFS(coord[1:], memo)
#print(DFS(low_coord))

for coord in low_coord:
    print(list(coord))
    bas[coord] = DFS(succ(coord))

print(bas)






    

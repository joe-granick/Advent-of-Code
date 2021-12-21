#####--------------I'm Melting---------####
####PART 1##########################################
###############------Import data----------------####
from collections import defaultdict
with open("test_input.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()
length = len(lines)
end_line = length-1
width = len(lines[0])
end_height = width-1
basins = {} 
low_points = []
basin = 0
all_coord = []
def start_state():
    return  (0,0)

def isEnd(explored, length, width):
    return len(explored) == length*width 
  
def succession(coordinate, action):
    x = coordinate[0] + action[0]
    y = coordinate[1] + action[1]
    new_coord = (x, y)
    return new_coord

def actions(coordinates):
    grid = lines
    actions = []
    x = coordinates[0]
    y = coordinates[1]
    if x > 0 and (x-1, y) not in explored: actions.append((-1, 0))
    if y > 0 and (x, y-1) not in explored: actions.append((0, -1))
    if coordinates[0]+1 < end_height and (x+1, y) not in explored: actions.append((1, 0))
    if coordinates[1] < end_line and (x, y-+) not in explored: actions.append((0, 1))
    return actions

def frontier(state):
    frontier = []
    for action in actions(state): 
         frontier.append(succession(state, action))
    return frontier

explored = []
frontier = []
for y in range(len(lines)-1):
     for x in range(len(lines[y])-1):
         if int(lines[y][x]) == 9: explored.append((x,y))
         #else: frontier.append((x,y))



print(explored)
state = start_state()


#while not isEnd(explored, length, width):
for y in range(len(lines)-1):
     for x in range(len(lines[y])-1):
         front = frontier(state)
         if len(front) > 0:
#     #print(frontier)
#     explored.append(state)
#     print(explored)
#     if len(frontier)>0: state = frontier.pop(0)



    




# for y in range(len(lines)):
#     coordinates = []
#     for x in range(len(lines[i])-1):
#         coord = (x, y)
#         if coord not in all_coord:
#             all_coord.append(coord)
#             coordinates.append(coord)
#             moves = actions(coord)
#             for move in moves:
#                 if int(lines[y+moves[1]][x+moves[0]]) < 9:



# print(low_points)
# total = 0
# for i in low_points:
#     total += int(i)+1
# print(total)




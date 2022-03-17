#####--------------I'm Melting---------####
####PART Cheapest Path##########################################
###############------Import data----------------####
from collections import defaultdict
with open("test_input.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()

#print(lines)


current_min_risk = {}
for y in range(len(lines)):
    for x in range(len(lines[y])):
        print("Coordinate: ", (x, y), "\n", "Cost: " , lines[y][x])
        current_min_risk[(x,y)] = float('inf')

print(current_min_risk)

lowest_risk = {}





# def actions(coordinates):
#     actions = []
#     if coordinates[0] > 0:
#         actions.append((-1, 0))
#     if coordinates[1] > 0:
#         actions.append((0, -1))
#     if coordinates[0]+1 < end_height:
#         actions.append((1, 0))
#     if coordinates[1] < end_line:
#         actions.append((0, 1))
#     return actions

# for i in range(len(lines)):
#     coord = None
#     for h in range(len(lines[i])-1):
#         coord = (h, i)
#         moves = actions(coord)
#         count = 0
#         print(low_points)
#         print(moves)
#         print("y: ", i)
#         print("x: ", h)
#         for move in moves:
#            # print("Vertical Move:", move[1])
#             #print("Horizontal Move: ", move[0])
#             if lines[i][h] < lines[i + move[1]][h + move[0]]:
#                 count +=1
#             if count == len(moves):
#                 low_points.append(lines[i][h])
#                 low_coord.append((h, i))

# print(low_points)
# print(low_coord)
# total = 0
# for i in low_points:
#     total += int(i)+1
# print(total)




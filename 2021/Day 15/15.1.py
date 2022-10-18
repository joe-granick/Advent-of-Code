
#### Minimizing total decision risk#########################################
###############------Import data------------####
from collections import defaultdict
import heapq
with open("C:/Users/jmgra/OneDrive/Documents/advent_of_code/2021/Day 15test_input.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()

print(lines)

#model as weighted graph
#dijkstra's algorthim
#coordinates are vertices
#values are edge weights


# coordinate_risk = {} #risk of visiting individual coordinate
# current_min_risk = {} #current minimum total path risk of visiting a coordinate from the initital coordinate
# known_coordinates = [] #coordinate that have been discovered but not yet visited but have not been explored remove once visited
# visited_coordinates = {} #coordinates that have been visited and have ahd subsquent path coordinates calculated
# previous_coord_min_risk = {} #for the current coordinate returns previous coordinate from which visiting has the current lowest total path rsik 
# accumulated_risk = 0
# current_coordinate = (0,0)

# #initialize risk levels
# for y in range(len(lines)):
#     for x in range(len(lines[y])):
#         print("Coordinate: ", (x, y), "\n", "Cost: " , lines[y][x])
#         current_min_risk[(x,y)] = float('inf') #initialize total path risk to coordinate as +infintity
#         coordinate_risk[(x,y)] = lines[y][x] # create lookup table for individual coordinate risks
# current_min_risk[(0,0)] = 0 #initialize first coordinate with zero risk


# def newly_discovered_coords(graph, next_coord, coord_risk, unexplored_coords = []):
#     x1, y1 = next_coord[1], next_coord[2]
#     if x1 + 1 <= len(graph[0]):
#         horizontal = (x1 + 1, y1)
#     if y1 + 1 <= len(graph):
#         vertical = (x1, y1+1)
#     if horizontal and vertical:
#         heapq.heappush(unexplored_coords, vertical)
#         heapq.heappush(unexplored_coords, horizontal)
#     elif horizontal:
#         heapq.heappush(unexplored_coords, horizontal)
#     elif vertical:
#         heapq.heappush(unexplored_coords, vertical)
#     return unexplored_coords

# unexplored_coords = []
# previous_coord = (0, 0)

# while unexplored_coords:
#     coord = unexplored_coords.pop(0)
#     accumulated_risk += coordinate_risk[coord]
#     if accumulated_risk < current_min_risk[coord]:
#         current_min_risk[coord] = accumulated_risk
#         previous_coord_min_risk[coord] = previous_coord
#         previous_coord = coord











# # def actions(coordinates):
# #     actions = []
# #     if coordinates[0] > 0:
# #         actions.append((-1, 0))
# #     if coordinates[1] > 0:
# #         actions.append((0, -1))
# #     if coordinates[0]+1 < end_height:
# #         actions.append((1, 0))
# #     if coordinates[1] < end_line:
# #         actions.append((0, 1))
# #     return actions

# # for i in range(len(lines)):
# #     coord = None
# #     for h in range(len(lines[i])-1):
# #         coord = (h, i)
# #         moves = actions(coord)
# #         count = 0
# #         print(low_points)
# #         print(moves)
# #         print("y: ", i)
# #         print("x: ", h)
# #         for move in moves:
# #            # print("Vertical Move:", move[1])
# #             #print("Horizontal Move: ", move[0])
# #             if lines[i][h] < lines[i + move[1]][h + move[0]]:
# #                 count +=1
# #             if count == len(moves):
# #                 low_points.append(lines[i][h])
# #                 low_coord.append((h, i))

# # print(low_points)
# # print(low_coord)
# # total = 0
# # for i in low_points:
# #     total += int(i)+1
# print(total)




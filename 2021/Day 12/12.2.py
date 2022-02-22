#####--------------I'm Melting---------####
####PART 1##########################################
#########------Import data----------------####
from collections import defaultdict
from io import IncrementalNewlineDecoder
with open("input.txt", "r", encoding="utf-8") as f:
    graph = f.readlines()
for cave in graph:
    print(cave.strip())

movements = {}
small_cave = []
large_cave =[]
start = []
end = []

for cave in graph:
    states = cave.strip().split("-")
    cave_1, cave_2 = states[0], states[1]

    if cave_1 not in movements: movements[cave_1] = []
    if cave_2 not in movements: movements[cave_2] = []

    if cave_2 != 'start': movements[cave_1].append(cave_2)
    if cave_1 != 'start': movements[cave_2].append(cave_1)
    
    if cave_1.isupper() == True and cave_1 not in large_cave: 
        large_cave.append(cave_1)
    elif cave_1.islower() == True and cave_1 not in small_cave: 
        small_cave.append(cave_1)

    if cave_2.isupper() == True and cave_2 not in large_cave: 
        large_cave.append(cave_2)
    elif cave_2.islower() == True and cave_2 not in small_cave: 
        small_cave.append(cave_2)
print(movements)
print(small_cave)
#print(large_cave)
movements['end'] = []

def actions(state, caves_visited):
    next_moves = []
    for succession in movements[state]:
        if succession not in small_cave:
            next_moves.append(succession)
        elif max(caves_visited.values()) < 2:
            next_moves.append(succession)
        elif caves_visited[succession] < 1:
            next_moves.append(succession)
    return next_moves


caves_visited = {}
for cave in small_cave:
    caves_visited[cave] = 0

def find_path(path = [], moves = [], small_caves_visited = {}):
    if path == []:
        path.append('start')
        moves = actions('start', small_caves_visited)
    if path[-1] == 'end':
        return [path]
    elif moves == []:
        #print(path)
        return []
    else:
        #print(twice)
        first_move = moves.pop()
        state = path[-1]
        #if first_move in small_cave:
         #   caves_visited[state] += 1
        newly_visited = small_caves_visited.copy()
        #if state in small_cave:
         #   newly_visited[state] += 1 
        if first_move in small_cave:
            newly_visited[first_move] +=1 
        first_route = path + [first_move]
        next_moves = actions(first_move, newly_visited)
        return find_path(first_route, next_moves, newly_visited) + find_path(path, moves, small_caves_visited)

def valid_paths(paths):
    all_valid_paths = []
    for path in paths:
        if path not in all_valid_paths and path[-1] == 'end': all_valid_paths.append(path)
    return all_valid_paths

    


all_paths = find_path([],[],caves_visited)
print(len(all_paths))
#paths = valid_paths(all_paths)
#print(len(paths))
for path in all_paths:
    print(path)
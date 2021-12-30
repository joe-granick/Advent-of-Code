#####--------------I'm Melting---------####
####PART 1##########################################
#########------Import data----------------####
from collections import defaultdict
from io import IncrementalNewlineDecoder
with open("small_test_input.txt", "r", encoding="utf-8") as f:
    graph = f.readlines()
for cave in graph:
    print(cave.strip())

movements = {}
small_cave = []
large_cave =[]
start = []
end = []
dead_end = []
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
#print(small_cave)
#print(large_cave)
movements['end'] = []

def actions(state, caves_visited):
    next_moves = []
    for succession in movements[state]:
        if succession not in small_cave or caves_visited[succession] == False:
            next_moves.append(succession)
    return next_moves


def endState(movements, path):
    path_state = {"dead end": False, "end": False}
    if movements == []:
        path_state["dead end"] = True
    elif movements[-1] == "end":
        path_state["end"] = True    
    return path_state

caves_visited = {}
for cave in small_cave:
    caves_visited[cave] = False

def find_path(path = [], moves = [], small_caves_visited = {}):
    if path == []:
        path.append('start')
        moves = actions('start', small_caves_visited)
    if moves == []:
        #print(path)
        return [path]
    else:
        first_move = moves.pop()
        state = path[-1]
        newly_visited = small_caves_visited.copy()
        if state in small_cave:
            newly_visited[state] = True
        #print("new visit: ", newly_visited)
        #print("origin visit: ", small_caves_visited)
        first_route = path + [first_move]
        next_moves = actions(first_move, caves_visited = newly_visited)
        return find_path(first_route, next_moves, newly_visited)+ find_path(path, moves, small_caves_visited)

def valid_paths(paths):
    all_valid_paths = []
    for path in paths:
        if path[-1] == 'end': all_valid_paths.append(path)
    return all_valid_paths

    


all_paths = find_path([],[],caves_visited)

count = 0
for route in valid_paths(all_paths):
    print(route)
    count +=1
    print(count)
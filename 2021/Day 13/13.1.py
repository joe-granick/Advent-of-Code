#####--------------I'm Melting---------####
####PART 1##########################################
#########------Import data----------------####
from collections import defaultdict
from io import IncrementalNewlineDecoder
with open("input.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()

points = []
folds = []

for line in lines:
    if line[0] == 'f':
        folds.append(line.strip())
    else:
        if line[0] != '':
            points.append(line.strip('\n'))

#print(points)
print(folds)

#print(points[0][1])
print(folds[0][-1])
print(folds[1][-1])

coords = []
for point in points:
    if len(point) > 0:
        tup = tuple(map(int, point.split(",")))
        coords.append(tup)
#print(coords)

def y_fold(folds, coords):
    new_coords = []
    fold = int(folds[0][-1])
    for coord in coords:
        if coord[1] <= fold: new_coord = coord
        else: new_coord = (coord[0], fold + (fold - coord[1]))
        
        if new_coord not in new_coords:
            new_coords.append(new_coord)
    return new_coords

def x_fold(fold, coords):
    new_coords = []
    for coord in coords:
        if coord[0] <= fold: new_coord = coord
        else: new_coord = (fold + (fold - coord[0]), coord[1])
        
        if new_coord not in new_coords:
            new_coords.append(new_coord)
    return new_coords

# fold_test = y_fold(folds, coords)
# print(fold_test)
# print(len(fold_test))
# test = [(0,0), (2, 0), (3,0), (6,0), (9,0), (0,1), (4,1), (6,2), (10,2), (0,3), (4,3), (1,4), (3,4), (6,4),(8,4), (9,4),(10,4)]

# for point in test:
#     if point in fold_test:
#         print(point, " Included")
#     else:
#         print(point, " not included")

fold_test = x_fold(655, coords)
print(fold_test)
print(len(fold_test))

#test = [(0,0), (1, 0), (2, 0), (3, 0), (4,0), (0,1), (4,1), (0,2), (4,2), (0,3), (4,3), (0,4), (1, 4), (2, 4), (3, 4), (4,4)]
# print(len(test))
# for point in test:
#     if point in fold_test:
#         print(point, " Included")
#     else:
#         print(point, " not included")


    
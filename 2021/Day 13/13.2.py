#####--------------I'm Melting---------####
####PART 1##########################################
#########------Import data----------------####
import numpy as np
from matplotlib import pyplot as plt
from collections import defaultdict
from io import IncrementalNewlineDecoder
import re
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

foldRegex = re.compile(r'(y|x).*')
#print(points)
print(folds)
instructions = []
for fold in folds:
    instruction = foldRegex.search(fold)
    instructions.append(instruction.group())

print(instructions)
new_folds = []
for instruction in instructions:
    new_folds.append(instruction.split('='))


print(new_folds)



coords = []
for point in points:
    if len(point) > 0:
        tup = tuple(map(int, point.split(",")))
        coords.append(tup)

def y_fold(folds, coords):
    new_coords = []
    fold = int(folds[1])
    for coord in coords:
        if coord[1] <= fold: new_coord = coord
        else: new_coord = (coord[0], fold + (fold - coord[1]))
        if new_coord not in new_coords:
            new_coords.append(new_coord)
    return new_coords

def x_fold(folds, coords):
    new_coords = []
    fold = int(folds[1])
    for coord in coords:
        if coord[0] <= fold: new_coord = coord
        else: new_coord = (fold + (fold - coord[0]), coord[1])
        if new_coord not in new_coords:
            new_coords.append(new_coord)
    return new_coords

for fold in new_folds:
    print(fold)
    if fold[0] =='y':
         coords = y_fold(fold, coords)
    else:
        coords = x_fold(fold, coords)
print(coords)

y_max = 0
x_max = 0
for coord in coords:
    if coord[0] > x_max:
        x_max = coord[0]
    if coord[1] > y_max:
        y_max = coord[1]

rows = []

for y in range(y_max+1):
    row = []
    for x in range(x_max+1):
        if (x,y) in coords:
            row.append("#")
        else:
            row.append("-")
    rows.append(row)

#print(rows)

for row in rows:
    print(''.join(row))
# data = np.array(coords)
# x, y = data.T
# plt.scatter(x,y)
# plt.show()



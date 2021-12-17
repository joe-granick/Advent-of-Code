with open('input_1.txt') as f:
    lines = f.readlines()
increase = 0
total = 0
previous = float('inf')
for line in lines:
    if float(line) > previous:
        increase +=1
    previous = float(line)
    total +=1
print(increase)
print(total)

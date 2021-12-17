with open('input_1.txt') as f:
    lines = f.readlines()
increase = 0
total = 0
one = 0
two = 0
three = 0
current = 0
previous = float('inf')
for i in range(len(lines)):
    if i + 2 >= len(lines):
        print(increase)
        break
    else:
        one = float(lines[i])
        two = float(lines[i+1])
        three = float(lines[i+2])
        current = one + two + three
        if current > previous:
            increase +=1
        previous = current
        total +=1
print(increase)
print(total)

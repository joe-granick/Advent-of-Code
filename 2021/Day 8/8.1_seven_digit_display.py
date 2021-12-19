from collections import defaultdict
#####--------------CLOCK BLOCKING---------####

####PART 1##########################################

###############------Import data----------------####
with open("input.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()

clock = []
disp = []
for line in lines:
    clock.append(line.split("|")[0])
    disp.append(line.split("|")[1])
for i in range(len(clock)):
    clock[i] = clock[i].split()
for i in range(len(disp)):
    disp[i] = disp[i].split()

print(clock)
print(len(clock))
print(disp)
print(len(disp))

digits = {"zero": 0,
          "one": 0,
          "two": 0,
          "three": 0,
          "four": 0,
          "five": 0,
          "six": 0,
          "seven": 0,
          "eight": 0,
          "nine": 0}

print(digits)

for i in range(len(clock)):
    for digit in clock[i]:
        if len(digit) == 2:
            one = digit
    for display_digit in disp[i]:
        if one[0] in display_digit and one[1] in display_digit:
            if len(display_digit) == 2:
                   digits["one"] += 1
            elif len(display_digit) == 3:
                     digits["seven"] += 1
            elif len(display_digit) == 4:
                     digits["four"] += 1
            elif len(display_digit) == 7:
                digits["eight"] += 1
print(sum(digits.values()))
                    
                   
          









    

        

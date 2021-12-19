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

segments = {"a": 8, "b": 6, "c": 8, "d": 7, "e": 4, "f": 9, "g": 7}
segment_key = {"a": None, "b": None, "c": None, "d": None, "e": None, "f": None, "g": None}
zero = {"a": 1, "b": 1, "c": 1, "d": 0, "e": 1, "f": 1, "g": 1}
one = {"a": 0, "b": 0, "c": 1, "d": 0, "e": 0, "f": 1, "g": 0}
two = {"a": 1, "b": 0, "c": 1, "d": 1, "e": 1, "f": 0, "g": 1}
three = {"a": 1, "b": 0, "c": 1, "d": 1, "e": 0, "f": 1, "g": 1}
four = {"a": 0, "b": 1, "c": 1, "d": 1, "e": 0, "f": 1, "g": 0}
five = {"a": 1, "b": 1, "c": 0, "d": 1, "e": 0, "f": 1, "g": 1}
six = {"a": 1, "b": 1, "c": 0, "d": 1, "e": 1, "f": 1, "g": 1}
seven = {"a": 1, "b": 0, "c": 1, "d": 0, "e": 0, "f": 1, "g": 0}
eight = {"a": 1, "b": 1, "c": 1, "d": 1, "e": 1, "f": 1, "g": 1}
nine = {"a": 1, "b": 1, "c": 1, "d": 1, "e": 0, "f": 1, "g": 1}

digits = {"zero": 42, "one": 17, "two": 34, "three": 39, "four": 30, "five": 37, "six": 41, "seven": 25, "eight": 49, "nine": 45}

for i in range(len(clock)):
    scrambled_segments = defaultdict(lambda: 0)
    for segment in clock[i]:
        for letter in segment:
            scrambled_segments[letter] +=1
    for segment in clock[i]:
        if segment == 2:
            if scrambled[segment[0]] == 8:
                segment_key["c"] = segment[0]
                segment_key["f"] = segment[1]
            else:
                segment_key["c"] = scrambled[segment[1]]
                segment_key["f"] = scrambled[segment[0]]
    for segment in clock[i]:
        if segment == 3:
            for d in segment:
                if d not in segment_key.values():
                    segment_key["a"] = d
    
            
            
            

    print(scrambled_segments)
        



print(digits)

#for i in range(len(clock)):
#    for digit in clock[i]:
#        if len(digit) == 2:
#            one = digit
#    for display_digit in disp[i]:
#        if one[0] in display_digit and one[1] in display_digit:
#            if len(display_digit) == 2:
#                   digits["one"] += 1
#            elif len(display_digit) == 3:
#                     digits["seven"] += 1
#            elif len(display_digit) == 4:
#                     digits["four"] += 1
#            elif len(display_digit) == 7:
#                digits["eight"] += 1
#print(sum(digits.values()))
                    
                   
          









    

        

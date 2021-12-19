from collections import defaultdict
#####--------------CLOCK BLOCKING---------####

####PART 1##########################################

###############------Import data----------------####
with open("single_input.txt", "r", encoding="utf-8") as f:
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
digits = {42: "0",  17: "1" , 34: "2", 39: "3", 30: "4", 37: "5", 41 : "6", 25: "7", 49: "8", 45: "9"}
digit_count = {"zero": 0, "one": 0, "two": 0, "three": 0, "four": 0, "five": 0, "six": 0, "seven": 0, "eight": 0, "nine": 0}

def count_letters(reading):
    segment_count = {"a": 0, "b": 0, "c": 0, "d": 0, "e": 0, "f": 0, "g": 0}
    for segment in reading:
        for letter in segment:
            segment_count[letter] += 1
    return segment_count

def score_segment(segment, scores):
    score = 0
    for letter in segment:
        score += scores[letter]
    return score


total = 0
for i in range(len(clock)):
    counts = count_letters(clock[i])
    print(counts)
    display_score = ""
    for segment in disp[i]:
        score = score_segment(segment, counts)
        print(score)
        digit = str(digits[score])
        display_score += digit
        print(display_score)
        total += int(display_score)
        print(total)
print(total)

#print(digit_count)
#print(sum(digit_count.values()))
                    
                   
          









    

        

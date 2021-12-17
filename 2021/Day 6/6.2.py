from collections import defaultdict
#####--------------HORNY LANTERNFISH----------####


###############------Import data----------------####
with open("input.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()
#print(lines)
lines = lines[0].split(",")
print(lines)

school = defaultdict(lambda: 0)
for days in range(0,9):
    school[days] = 0 
for i in lines:
    day = int(i)
    school[day] += 1
print(school)


day = 256
count = 1
while day > 0:
    newfish = school[0]
    for k, v in school.items():
        if k == 8:
            school[k] = newfish
        elif k == 6:
            school[k] = newfish + school[7]
        else:
            school[k] = school[k+1]
    print("Day: ", count," Lanternfish: ", sum(school.values()))
    day -= 1
    count += 1








    

        

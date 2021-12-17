#####--------------HORNY LANTERNFISH----------####


###############------Import data----------------####
with open("input.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()

school = lines[0].split(",")
print(school)
for i in range(0, len(school)):
    school[i] = int(school[i])
print(school)

days = 256
day_count = 0
while days != 0:
    for i in range(0, len(school)):
        if school[i] == 0:
            school[i] = 6
            school.append(8)
        else:
            school[i] -= 1
    days -= 1
    day_count += 1
    print("Day: ", day_count," Fish: ", len(school))
        

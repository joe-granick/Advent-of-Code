
#########------Import data----------------####
from collections import defaultdict
from io import IncrementalNewlineDecoder
with open("test_input.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()


for line in lines:
    line = line.strip()
    print(line)

print(lines[2:])
print(lines[2][3])

polymer_template = lines.pop(0)
#print(polymer_template)

pair_insert = defaultdict(lambda: 'blank') #look up polymer to insert between pairs

print(lines[2:])
for line in lines[1:]:
    pair = line.split("->")
    print(pair[0])
    #print(pair[1])
    pair_insert[pair[0].strip()] = pair[1].strip("\n").strip()



def insert(template, lookup, polymer = ''):
    pair = template[:2]    
    # print(pair)
    # print(template)
    # print(polymer)
    if len(template) <= 2:
        polymer = polymer + pair
        return polymer
    else:
        polymer = polymer + template[0] + lookup[pair]
        return insert(template[1:], lookup, polymer)

new_polymer = insert(polymer_template, pair_insert)
print(new_polymer)
new_new_polymer = insert(new_polymer, pair_insert)
print(new_new_polymer)
print(pair_insert)

def polymerize(insertion, template, lookup, steps):
    if steps == 0:
        return template
    else:
        template = insertion(template, lookup)
        return polymerize(insertion, template, lookup, steps-1)
    
new_polymer = polymerize(insert, polymer_template, pair_insert, 10)
print(new_polymer)
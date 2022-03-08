
#########------Import data----------------####
from collections import defaultdict
from io import IncrementalNewlineDecoder
with open("test_input.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()

for line in lines:
    line = line.strip()
    print(line)

print(lines[0])
print(lines[2:])
print(lines[2][3])

initial_compound = lines.pop(0)
pair_insert = defaultdict(lambda: 'blank') #look up polymer to insert between pairs

print(lines[2:])
for line in lines[1:]:
    pair = line.split("->")
    print(pair[0])
    #print(pair[1])
    pair_insert[pair[0].strip()] = pair[1].strip("\n").strip()

expanded_pairs = {} #translate comppounds into reuslting pair after ploymerization
for k, v in pair_insert.items():
    expanded_pairs[k] = [str(k[0]) + str(v),str(v) + str(k[1])]
print(expanded_pairs)


pair_count = {}  #initaialize dictionary with compund pairs counted
for k in pair_insert.keys():
    pair_count[k] = 0
print(pair_count)

print(initial_compound)
initial_compound = 'NNCB'
for i in range(len(initial_compound)-1):
   # print(i, ": ", initial_compund[i])
    pair_count[initial_compound[i] + initial_compound[i+1]] += 1
    print(initial_compound[i] + initial_compound[i+1])

print(pair_count)

print(expanded_pairs['NN'][0])
print(expanded_pairs['NN'][1])
print(pair_count['NN'])

def polymerize(pair_counts, pair_expansion):
    pass
    new_pair_counts = defaultdict(lambda: 0)
    for key, val in pair_counts.items():
        if pair_counts[key] > 0:
            new_pair_1, new_pair_2 = pair_expansion[key][0], pair_expansion[key][1]
            new_pair_counts[new_pair_1] += val
            new_pair_counts[new_pair_2] += val
        #look up expansion for par represented in original compound
        #increment expansion pairs by multiple of original compund pair to create new compund
    return new_pair_counts

#calculate plymerization for i number of steps
i = 0
while i < 1:
    pair_count = polymerize(pair_count, expanded_pairs) 
    i+=1
print(pair_count)
#count unique letters
letter_count = defaultdict(lambda: 0)
for k, v in pair_count.items():
    letter_count[k[0]] += v
    letter_count[k[1]] += v
print(letter_count)


# initial_compound = 'NBCCNBBBCBHCB'
# test_pair = defaultdict(lambda: 0)
# print(initial_compound)
# for i in range(len(initial_compound)-1):
#     #print(i, ": ", initial_compund[i])
#     test_pair[initial_compound[i] + initial_compound[i+1]] += 1
#     print(initial_compound[i] + initial_compound[i+1])
# print(pair_count)
# print(test_pair)

# for k in pair_count.keys():
#     print(k, ": ", "Calculated: ",pair_count[k], "Test pair:", test_pair[k], " ", pair_count[k] == test_pair[k])
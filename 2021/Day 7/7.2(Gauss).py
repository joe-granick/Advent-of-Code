from collections import defaultdict
#####--------------WHALES WITH CRABS---------####

####PART 2##########################################

#Now costs increase with each move

###############------Import data----------------####
def fuel(start, end): 
    return ((end-start)*((end-start)+1))/2
    
with open("input.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()
lines = lines[0].split(",")
print(lines)

max_state = max(int(i) for i in lines)
print(max_state)
min_state =  min(int(i) for i in lines)
print(min_state)
distance = defaultdict(lambda: None)

print(fuel(0, 5))
print(fuel(1, 5))
print(fuel(2, 5))
print(fuel(5, 16))

for i in range(min_state, max_state+1):
    distance[i] = fuel(max_state-i, max_state)
print(distance)

states = defaultdict(lambda: 0)
costs = defaultdict(lambda: 0)

for i in range (min_state, max_state+1):
    costs[i] = 0
print(costs)

for i in lines:
    states[int(i)] += 1
print(states)

#cost = abs(state - next state) x crabs in that state 

for k in costs.keys():
    cost = 0
    for s, v in states.items():
        cost += v*distance[abs(s - k)]
    costs[k] = cost

print(costs)    
print(min(costs.values()))

    



#print(min(costs.values()))




    

        

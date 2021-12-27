#####--------------I'm Melting---------####
####PART 1##########################################
#########------Import data----------------####
from collections import defaultdict
from io import IncrementalNewlineDecoder
with open("test_input.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()
octopi = []
for line in lines:
    row = []
    for number in line.strip():
        number = int(number)
        row.append(number)
    octopi.append(row)
print(octopi)

def incr_flash_adjacent(coord, energy):
    new_flashes = []
    x = coord[0]
    y = coord[1] 
    energy[coord] = 0
    if (x+1, y) in energy.keys() and energy[(x+1, y)] <= 9:
        energy[(x+1, y)] +=1
        if energy[(x+1, y)] == 9: new_flashes.append((x+1, y))
    
    if (x-1, y) in energy.keys() and energy[(x-1, y)] <= 9:
        energy[(x - 1, y)] += 1
        if energy[(x-1, y)] == 9: new_flashes.append((x-1, y))
    
    if (x, y+1) in energy.keys() and energy[(x, y+1)] <= 9:
        energy[(x, y + 1)] +=1
        if energy[(x, y+1)] == 9: new_flashes.append((x, y+1))
    
    if (x, y-1) in energy.keys() and energy[(x, y-1)] <= 9: 
        energy[(x, y-1)] +=1
        if energy[(x, y-1)] == 9: new_flashes.append((x, y-1))
    
    if (x+1, y-1) in energy.keys() and energy[(x+1, y-1)] <= 9: 
        energy[(x+1, y-1)] += 1
        if energy[(x+1, y-1)] == 9: new_flashes.append((x+1, y-1))
    
    if (x+1, y+1) in energy.keys() and energy[(x+1, y+1)] <= 9:
        energy[(x+1, y+1)]+=1
        if energy[(x+1, y+1)] == 9: new_flashes.append((x+1, y+1))
    
    if (x-1, y-1) in energy.keys() and energy[(x-1, y-1)] <= 9:
        energy[(x -1, y-1)]+=1
        if energy[(x-1, y-1)] == 9: new_flashes.append((x-1, y-1))
    
    if (x - 1, y + 1) in energy.keys() and energy[(x - 1, y + 1)] <= 9:
        energy[(x - 1, y + 1)] +=1
        if energy[(x - 1, y + 1)] == 9: new_flashes.append((x - 1, y + 1))
    return (energy, new_flashes)

def flash_adj(coords, energy, flashed = []):
    if coords == []:
        return energy
    else:
        coord = coords.pop(0)
        if coord not in flashed:
            flashed.append(coord)
            energy, new_coords = incr_flash_adjacent(coord, energy)
            coords = coords + new_coords
        return flash_adj(coords, energy, flashed)


def incr_energy(energy, flashed):
    for coord in energy:
        if coord not in flashed:
            energy[coord] += 1
        else:
            coord = 0

    return energy

def scan_energy(octopi):
    energy_levels = {}
    for y in range(len(octopi)):
        for x in range(len(octopi[y])):
            energy_levels[(x, y)] = octopi[y][x]
    return energy_levels

#needs a rewrite
def new_flashes(energy, flashed = []):
    flashing_octopi = []
    for coord in energy.keys() :
        if energy[coord] >= 9 and coord not in flashed:
            flashing_octopi.append(coord)
    return flashing_octopi

def identity(x):
    return x

def flash_reaction(energy, flashed = []):
    flashing_energy = new_flashes(energy)
    flash_adjacent = flash_adj(flashing_energy, energy, flashed)
    flashed = flashing_energy
    print("Flash adjacent: ", flash_adjacent)
    return [flash_adjacent, flashed]

def flash_cycles(cycles = 0, energy = {}, n = 0):
    if n == cycles:
        return energy
    else:
        energy, flashed = flash_reaction(energy)
        print("Postreactionns: ", energy)
        incremented_energy = incr_energy(energy, flashed)
        n+=1
    return flash_cycles(cycles, incremented_energy, n)


#create initials scan of energy levels
octo_energy = scan_energy(octopi)
print("Octopi starting conditions:") 
for octopus, energ in octo_energy.items():
    print("Octopus: ",octopus, "Energy:  ", energ)

#Scan for flashes

flashing_energy = new_flashes(octo_energy)
print("Octopi that will flash:") 
for octopus in flashing_energy:
    print("Octopus: ",octopus, "Energy:  ", octo_energy[octopus])

octo_energy = scan_energy(octopi)

print("Octopi conditions after flash:")
print(flash_reaction(octo_energy))
#print(flashing_energy)
#coord = flashing_energy.pop(0)
#print(coord)
#print(incr_flash_adjacent(coord, energy))
post_flash = flash_adj(flashing_energy, octo_energy)
for octopus, energ in post_flash.items():
    print("Octopus: ",octopus, "Energy:  ", energ)



octo_energy = flash_cycles(cycles = 2, energy = octo_energy)
print(octo_energy)

max_y = 0
max_x = 0
for key in octo_energy.keys():
    x = key[0]
    y = key[1]
    if x > max_x: max_x = x
    if y > max_y: max_y = y
print(max_x, max_y)

grid = []
blanks = []
for y in range(0, max_y+1):
    blanks.append(0)
print(blanks)

for x in range(0, max_x+1):
    grid.append(blanks.copy())

for y in range(0, max_y+1):
    for x in range(0, max_x+1):
        print(octo_energy[(x,y)])

for row in grid:
    print(row)





        
            
            



      
      
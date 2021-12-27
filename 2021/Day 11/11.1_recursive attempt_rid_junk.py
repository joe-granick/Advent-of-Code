#####--------------I'm Melting---------####
####PART 1##########################################
#########------Import data----------------####
from collections import defaultdict
from io import IncrementalNewlineDecoder
with open("input.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()
octopi = []
for line in lines:
    row = []
    for number in line.strip():
        number = int(number)
        row.append(number)
    octopi.append(row)
print(octopi)

def incr_flash_adjacent(coord, energy, flashed = []):
    new_flashes = []
    x = coord[0]
    y = coord[1] 
    energy[coord] = 0
    if (x+1, y) in energy.keys() and energy[(x+1, y)] <= 9 and (x+1, y) not in flashed:
        energy[(x+1, y)] +=1
        if energy[(x+1, y)] >= 9: new_flashes.append((x+1, y))
    
    if (x-1, y) in energy.keys() and energy[(x-1, y)] <= 9 and (x-1, y) not in flashed:
        energy[(x-1, y)] += 1
        if energy[(x-1, y)] >= 9: new_flashes.append((x-1, y))
    
    if (x, y+1) in energy.keys() and energy[(x, y+1)] <= 9 and (x, y+1) not in flashed:
        energy[(x, y+1)] +=1
        if energy[(x, y+1)] >= 9: new_flashes.append((x, y+1))
    
    if (x, y-1) in energy.keys() and energy[(x, y-1)] <= 9 and (x, y-1) not in flashed: 
        energy[(x, y-1)] +=1
        if energy[(x, y-1)] >= 9: new_flashes.append((x, y-1))
    
    if (x+1, y-1) in energy.keys() and energy[(x+1, y-1)] <= 9 and (x+1, y-1) not in flashed: 
        energy[(x+1, y-1)] += 1
        if energy[(x+1, y-1)] >= 9: new_flashes.append((x+1, y-1))
    
    if (x+1, y+1) in energy.keys() and energy[(x+1, y+1)] <= 9 and (x+1, y+1) not in flashed:
        energy[(x+1, y+1)]+=1
        if energy[(x+1, y+1)] >= 9: new_flashes.append((x+1, y+1))
    
    if (x-1, y-1) in energy.keys() and energy[(x-1, y-1)] <= 9 and (x-1, y-1) not in flashed:
        energy[(x -1, y-1)]+=1
        if energy[(x-1, y-1)] >= 9: new_flashes.append((x-1, y-1))
    
    if (x - 1, y + 1) in energy.keys() and energy[(x - 1, y + 1)] <= 9 and (x - 1, y + 1) not in flashed:
        energy[(x - 1, y + 1)] +=1
        if energy[(x - 1, y + 1)] >= 9: new_flashes.append((x - 1, y + 1))
    return (energy, new_flashes)

def flash_adj(coords, energy, flashed = []):
    if coords == []:
        return [energy, flashed]
    else:
        coord = coords.pop(0)
        if coord not in flashed:
            flashed.append(coord)
            energy, new_coords = incr_flash_adjacent(coord, energy, flashed)
            energy[coord] = 0
            coords = coords + new_coords
            print("flashed: ", flashed)
            print_grid(energy)
        return flash_adj(coords, energy, flashed)


def incr_energy(energy, initial_flash):
    for coord in energy.keys():
        if coord not in initial_flash:
            energy[coord] += 1
    return energy

def scan_energy(octopi):
    energy_levels = {}
    for y in range(len(octopi)):
        for x in range(len(octopi[y])):
            energy_levels[(x, y)] = octopi[y][x]
    return energy_levels

def new_flashes(energy, flashed = []):
    flashing_octopi = []
    for coord in energy.keys() :
        if energy[coord] >= 9 and coord not in flashed:
            flashing_octopi.append(coord)
    return flashing_octopi

def identity(x):
    return x

def flash_reaction(energy, flashed=[]):
    flash_adjacent, flashed = flash_adj(new_flashes(energy), energy, flashed)
    print("Flash adjacent: ", flash_adjacent)
    return [flash_adjacent, flashed]


#Need to set up initialincrement 
def flash_cycles(cycles = 0, energy = {}, n = 0, flash_count = 0):
    if n ==cycles: 
        print("Cycle: ", n)
        print("Flashes: ", flash_count)
        print_grid(energy)
        return energy
    else:
        print("First set: ", n)
        #print_grid(energy)
        energy, flashed = flash_reaction(energy, flashed = [])
        energy = incr_energy(energy, flashed)
        print("Flashed: ", flashed)
        flash_count += len(flashed)
        n+=1
    return flash_cycles(cycles, energy, n, flash_count)

def print_grid(octo_energy):
    max_y = 0
    max_x = 0
    for key in octo_energy.keys():
        x = key[0]
        y = key[1]
        if x > max_x: max_x = x
        if y > max_y: max_y = y
    grid = []
    blanks = []
    for y in range(0, max_y+1):
        blanks.append(0)
    for x in range(0, max_x+1):
        grid.append(blanks.copy())
    for y in range(0, max_y+1):
        for x in range(0, max_x+1):
            grid[y][x] = octo_energy[(x,y)]
    for row in grid:
        print(row)


#create initials scan of energy levels
octo_energy = scan_energy(octopi)
flash_cycles(cycles = 100, energy = octo_energy)

#print(new)








        
            
            



      
      
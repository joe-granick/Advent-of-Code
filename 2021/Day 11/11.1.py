#####--------------I'm Melting---------####
####PART 1##########################################
#########------Import data----------------####
from collections import defaultdict
with open("adv_test_input.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()
octopi = []
for line in lines:
    row = []
    for number in line.strip():
        number = int(number)
        row.append(number)
    octopi.append(row)

def flashes(coord, energy):
    x = coord[0]
    y = coord[1] 
    if (x+1, y) in energy.keys():
        energy[(x+1, y)] +=1
    if (x-1, y) in energy.keys():
        energy[(x - 1, y)] += 1
    if (x, y+1) in energy.keys():
        energy[(x, y + 1)] +=1
    if (x, y-1) in energy.keys(): 
        energy[(x, y-1)] +=1
    if (x+1, y - 1) in energy.keys(): 
        energy[(x + 1, y - 1)] += 1
    if (x+1, y+1) in energy.keys():
        energy[(x+1, y+1)]+=1
    if (x -1, y-1) in energy.keys():
        energy[(x -1, y-1)]+=1
    if (x - 1, y + 1) in energy.keys():
        energy[(x - 1, y + 1)] +=1
    return energy
def incr_energy(octo, incremented_row = None):
    if not incremented_row:
        incremented_row = []
    if not octo:
        return incremented_row
    else:
        inc = octo[0]
        if inc == 9:
            inc = 9
        else:
            inc += 1
        incremented_row.append(inc)
        return incr_energy(octo[1:], incremented_row[:])
def traverse_row(octopi, new_octopi = None):
    if not new_octopi:
        new_octopi = []
    if not octopi:
        return new_octopi
    else:
        row = octopi[0]
        new_energy = incr_energy(row)
        new_octopi.append(new_energy)
        return traverse_row(octopi[1:], new_octopi[:])
def scan_octopus_energy(octopi):
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


energy = scan_octopus_energy(octopi)
print(energy)
flashing_oct = []
n = 10
i = 1
flash_count = 0
loop_flash = False
while i <= n:
    print("\n")
    flashed = []
    for coord in energy.keys():
        if energy[coord] >= 9:
            flashing_oct.append(coord)
            energy[coord] = 0
        else: energy[coord] += 1
    print("Flashes: ", flashing_oct)
    print(len(flashing_oct))
    flash_count+= len(flashing_oct)
    if len(flashing_oct) > 0: loop_flash = True
    while loop_flash:
        for octo in flashing_oct:
            energy[octo] = 0
            flashed.append(octo)
            energy = flashes(octo, energy)
        flashing_oct = []
        new_flash = new_flashes(energy, flashed)
        for octo in new_flash:
            flashing_oct.append(octo)
        #flash_count += len(flashing_oct)
        if flashing_oct == []: loop_flash = False
        print("energy: ", energy)
        print("\n")
    print(energy)
    i+=1
    print("next turn:", i)
    print("\n")
    print("Flashes: ", flash_count)
for k, v in energy.items():
     print(k, v)
print(flash_count)
   


        
            
            



      
      
with open('input.txt') as f:
    lines = f.readlines()


def convert_dig(bit):
    max_power = len(bit)-1
    dig = 0
    for i in range(len(bit)):
        if bit[i] == 1:
            dig = dig + 2**(max_power-i)
    return dig
print(convert_dig([1,0,1,1,0]) )
print(convert_dig([0,1,0,0,1]) ) 

#binary = {'zero': 0, 'one': 0}
digits = []
ones = {}
one = 0
line_iter = 0

for i in range(len(lines[0])-1):
    if len(digits) <= i:
        digits.append({'zero': 0, 'one': 0})

for line in lines:
    for i in range(len(line)-1):
        bit = int(line[i])
        if bit == 0:
            digits[i]['zero'] += 1
        else:
            digits[i]['one'] += 1
    line_iter +=1

print(line_iter)


        

gamma = []
epsilon = []

for i in digits:
    if i['zero'] > i['one']:
        gamma.append(0)
        epsilon.append(1)
    else:
        gamma.append(1)
        epsilon.append(0)
print(gamma)
print(epsilon)


print(convert_dig(gamma))
print(convert_dig(epsilon))
print(convert_dig(gamma)*convert_dig(epsilon))


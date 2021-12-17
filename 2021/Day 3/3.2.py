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

def bit_count (lines):
    digits = []
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
    return digits
digits = bit_count(lines)
print(digits)


def gamma_epsilon(digits):
    gamma = []
    epsilon = []
    for i in digits:
        if i['zero'] > i['one']:
            gamma.append(0)
            epsilon.append(1)
        else:
            gamma.append(1)
            epsilon.append(0)
    return {'gamma': gamma, 'epsilon': epsilon}
gamma = gamma_epsilon(digits)['gamma']
epsilon = gamma_epsilon(digits)['epsilon']
print(gamma)
print(epsilon)
print(convert_dig(gamma))
print(convert_dig(epsilon))
print(convert_dig(gamma)*convert_dig(epsilon))


def o2_read(lines, i, bitcount):
    digits = bitcount(lines)
    if len(lines) == 1:
        return lines
    print(digits)
    if len(lines) > 1:
        if digits[i]['zero'] > digits[i]['one']:
            lines = list(filter(lambda line: line[i] == '0', lines))
            i+= 1
        else:
            lines = list(filter(lambda line: line[i] == '1', lines))
            i+=1
        return o2_read(lines, i, bitcount)
    else:
        return lines

def co2_read(lines, i, bitcount):
    digits = bitcount(lines)
    if len(lines) == 1:
        return lines
    print(digits)
    if len(lines) > 1:
        if digits[i]['zero'] <= digits[i]['one']:
            lines = list(filter(lambda line: line[i] == '0', lines))
            i+= 1
        else:
            lines = list(filter(lambda line: line[i] == '1', lines))
            i+=1
        return co2_read(lines, i, bitcount)
    else:
        return lines

def split(word):
    return [int(char) for char in word]

o2 = o2_read(lines, 0, bit_count)[0]
co2 = co2_read(lines, 0, bit_count)[0]
print(o2)
print(co2)
o2 = split(o2.strip())
co2 = split(co2.strip())
print(o2)
print(convert_dig(o2))
print(co2)
print(convert_dig(co2))


print(convert_dig(co2)*convert_dig(o2))

#co2_read(lines, [], 0, bit_count)
#print(convert_dig(o2)*convert_dig(co2))





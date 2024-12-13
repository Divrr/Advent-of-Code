def is_safe(sequence):
    previous = sequence[0]
    sign = -1 if sequence[1]-previous < 0 else 1

    for current in sequence[1:]:
        difference = current - previous
        if abs(difference) > 3 or abs(difference) < 1: return False
        if difference * sign < 0: return False
        previous = current
    
    return True

count = 0

f = open('2024/2.txt', 'r')

for line in f.readlines():
    sequence = [int(n) for n in line.split()]
    if is_safe(sequence): count += 1

print(count)
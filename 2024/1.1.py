def pair_distance(left, right):
    left.sort()
    right.sort()

    count = 0

    for i in range(len(left)):
        count += abs(left[i] - right[i])
    
    return count

# --------------------------------------
f = open("2024/1in.txt", "r")
left, right = [], []

for line in f.readlines():
    l, r = [int(n) for n in line.split()]
    left.append(l)
    right.append(r)

print(pair_distance(left, right))
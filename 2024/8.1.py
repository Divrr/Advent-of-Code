file = open("2024/8.txt", "r")
lines = file.readlines()
file.close()

frequencypos = {}
for x, line in enumerate(lines):
    for y, char in enumerate(list(line)):
        if char == "." or char == "#": continue
        frequencypos[char] = frequencypos.get(char, []) + [(x, y)]
       
visited = set()
height = len(lines)
width = len(lines[0].strip())
print(width, height)

for frequency, positions in frequencypos.items():
    for A in positions:
        for B in positions:
            if A == B: continue
            # find vector AB, then add it to B
            AB = (B[0]-A[0], B[1]-A[1])
            newpos = (B[0]+AB[0], B[1]+AB[1])
            if newpos[0] < 0 or newpos[0] >= width or newpos[1] < 0 or newpos[1] >= height: continue
            visited.add(newpos)

print(len(visited))
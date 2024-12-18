file = open("2024/6.txt", "r")
lines = file.readlines()
file.close()

frequencypos = {}
for x, line in enumerate(lines):
    for y, char in enumerate(list(line)):
        if char == ".": continue
        frequencypos[char] = frequencypos.get(char, []) + [(x, y)]
       
visited = set()
height = len(file.split("\n"))
width = len(file.split("\n")[0])

for frequency, positions in frequencypos.items():
      for A in positions:
            for B in positions:
                  if A == B: continue
                  # find vector AB, then add it to B
                  AB = (B[0]-A[0], B[1]-A[1])
                  newpos = (B[0]+AB[0], B[1]+AB[1])
                  print(A, B, AB, newpos)
                  if newpos[0] < 0 or newpos[0] >= height or newpos[1] < 0 or newpos[1] >= width: continue
                  visited.add(newpos)

print(len(visited))
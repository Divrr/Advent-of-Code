# I did this with DP and then deleted it so- I'm just gonna use DFS without the visited set instead. Performance doesn't matter anyway :skull:
file = open("2024/10.txt", "r")
lines = file.readlines()
file.close()

matrix = []

for line in lines:
    matrix.append([int(n) for n in list(line.strip())])

def score(matrix, start):
    count = 0
    stack = [start]

    while stack:
        xv, yv = stack.pop()
        if matrix[xv][yv] == 9: count += 1

        for direction in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
            x, y = direction
            xu, yu = xv + x, yv + y
            if xu < 0 or xu >= len(matrix) or yu < 0 or yu >= len(matrix[0]): continue

            if matrix[xu][yu] == matrix[xv][yv] + 1:
                stack.append((xu, yu))
    
    return count

startpositions = []
for i, line in enumerate(lines):
    for j, char in enumerate(list(line.strip())):
        n = int(char)
        if n == 0: startpositions.append((i, j))

s = 0
for startposition in startpositions:
    s += score(matrix, startposition)

print(s)
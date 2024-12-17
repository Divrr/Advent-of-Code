file = open("2024/6.txt", "r")

# SETUP
directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
direction = None
position = None
matrix = []

for i, row in enumerate(file):
    result = []
    for j, element in enumerate(row.strip()):
        if element in ["^", "v", ">", "<"]:
            symbols = ["^", "v", ">", "<"]
            position = (i, j)
            direction = directions[symbols.index(element)]
            result.append(".")
            continue
        result.append(element)

    matrix.append(result)

file.close()


visited = set()

while True:
    visited.add(position)

    # wall-check
    next_position = (position[0] + direction[0], position[1] + direction[1])
    if matrix[next_position[0]][next_position[1]] == "#":
            directionindex = (directions.index(direction) + 1) % 4
            direction = directions[directionindex]

    position = (position[0] + direction[0], position[1] + direction[1])

    # bound check
    if position[0] < 0 or position[1] < 0 or position[0] > len(matrix) or position[1] > len(matrix[1]):
        break

print(len(visited))
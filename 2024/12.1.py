from collections import deque
grid = [[char for char in line.strip()] for line in open("2024/12.txt", "r")]

def find_area_permieter(start, grid):
    perimeter = 0
    area = 0

    queue = deque([start])
    visited = {start}
    letter = grid[start[0]][start[1]]

    while queue:
        current = queue.pop()
        area += 1
        rv, cv = current

        for neighbour in [(rv+1, cv), (rv-1, cv), (rv, cv-1), (rv, cv+1)]:
            ru, cu = neighbour

            if ru < 0 or cu < 0 or ru >= len(grid) or cu >= len(grid[0]) or grid[ru][cu] != letter:
                perimeter += 1 
                continue

            if (ru, cu) in visited: continue
            
            queue.append((ru, cu))
            visited.add((ru, cu))
    
    return area, perimeter, visited

not_visited = set()

for i in range(len(grid)):
    for j in range(len(grid[0])):
        not_visited.add((i, j))

result = 0
while not_visited:
    region_start = not_visited.pop()
    area, perimeter, visited = find_area_permieter(region_start, grid)
    result += area*perimeter
    not_visited = not_visited - visited

print(result)
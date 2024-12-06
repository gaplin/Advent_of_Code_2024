def get_visited_positions(grid: list, n: int, position: tuple) -> int:
    visited = set()
    dir = (-1, 0) # (-1, 0), (0, 1), (1, 0), (0, -1) => (x, y) -> (y, -x)
    while True:
        visited.add(position)
        while True:
            i, j = position[0] + dir[0], position[1] + dir[1]
            if i < 0 or i >= n or j < 0 or j >= n:
                return visited
            if grid[i][j] == '.' or grid[i][j] == '^':
                position = (i, j)
                break
            dir = (dir[1], -dir[0])
        
def loop_created(grid: list, n: int, position: tuple) -> bool:
    visited = set()
    dir = (-1, 0) # (-1, 0), (0, 1), (1, 0), (0, -1) => (x, y) -> (y, -x)
    while True:
        while True:
            if (position, dir) in visited:
                return True
            visited.add((position, dir))
            i, j = position[0] + dir[0], position[1] + dir[1]
            if i < 0 or i >= n or j < 0 or j >= n:
                return False
            if grid[i][j] == '.' or grid[i][j] == '^':
                position = (i, j)
                break
            dir = (dir[1], -dir[0])


grid = open('input2.txt').read().splitlines()
n = len(grid)
for i in range(n):
    grid[i] = [x for x in grid[i]]

visited = set()
pos = (-1, 0)
for i in range(n):
    for j in range(n):
        if grid[i][j] == '^':
            pos = (i, j)
            break
    if pos[0] != -1:
        break

result = 0
for i, j in get_visited_positions(grid, n, pos):
    if grid[i][j] == '^':
        continue
    grid[i][j] = '#'
    if loop_created(grid, n, pos):
        result += 1
    grid[i][j] = '.'
print(result)
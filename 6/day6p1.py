def get_visited_positions(grid: list, n: int, position: tuple) -> int:
    visited = set()
    dir = (-1, 0) # (-1, 0), (0, 1), (1, 0), (0, -1) => (x, y) -> (y, -x)
    while True:
        visited.add(position)
        while True:
            i, j = position[0] + dir[0], position[1] + dir[1]
            if i < 0 or i >= n or j < 0 or j >= n:
                return len(visited)
            if grid[i][j] == '.' or grid[i][j] == '^':
                position = (i, j)
                break
            dir = (dir[1], -dir[0])
        

grid = open('input2.txt').read().splitlines()

n = len(grid)
visited = set()
pos = (-1, 0)
for i in range(n):
    for j in range(n):
        if grid[i][j] == '^':
            pos = (i, j)
            break
    if pos[0] != -1:
        break

print(get_visited_positions(grid, n, pos))
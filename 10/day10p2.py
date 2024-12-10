from queue import Queue

def BFS(grid: list, n: int, i: int, j: int) -> int:
    Q = Queue()
    Q.put((i, j))
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    nines = 0
    while Q.empty() == False:
        i, j = Q.get()
        if grid[i][j] == 9:
            nines += 1
        else:
            for di, dj in directions:
                new_i, new_j = i + di, j + dj
                if new_i < 0 or new_i >= n or new_j < 0 or new_j >= n or grid[i][j] + 1 != grid[new_i][new_j]:
                    continue
                Q.put((new_i, new_j))

    return nines


grid = open('input2.txt').read().splitlines()
n = len(grid)


result = 0
for i in range(n):
    grid[i] = [int(x) for x in grid[i]]

for i in range(n):
    for j in range(n):
        if grid[i][j] == 0:
            trails = BFS(grid, n, i, j)
            result += trails

print(result)

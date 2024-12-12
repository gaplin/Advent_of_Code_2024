from queue import Queue

def get_fences_cost(grid: list, n: int, i: int, j: int, visited: set) -> int:
    q = Queue()
    q.put((i, j))
    area = 0
    perimeter = 0
    visited.add((i, j))
    while q.empty() == False:
        (i, j) = q.get()
        area += 1
        for new_i, new_j in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
            if new_i < 0 or new_i >= n or new_j < 0 or new_j >= n or grid[new_i][new_j] != grid[i][j]:
                perimeter += 1
                continue
            if (new_i, new_j) not in visited:
                visited.add((new_i, new_j))
                q.put((new_i, new_j))

    return area * perimeter

grid = open('input2.txt').read().splitlines()
n = len(grid)

visited = set()
result = 0
for i in range(n):
    for j in range(n):
        if (i, j) not in visited:
            result += get_fences_cost(grid, n, i, j, visited)

print(result)

def starting_points(grid: list, i: int, j: int, target: str, n: int, m: int, s: int) -> int:
    directions = [(1, 0), (0, 1), (-1, 0), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]
    result = 0
    for di, dj in directions:
        new_i = i - di
        new_j = j - dj
        match_idx = 0
        for _ in range(s):
            new_i += di
            new_j += dj
            if new_i < 0 or new_i >= n or new_j < 0 or new_j >= m or grid[new_i][new_j] != target[match_idx]:
                break
            match_idx += 1
        else:
            result += 1
    return result

grid = open('input2.txt').read().splitlines()
n = len(grid)
m = len(grid[0])

result = 0
for i in range(n):
    for j in range(m):
        result += starting_points(grid, i, j, 'XMAS', n, m, 4)

print(result)
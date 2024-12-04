
def starting_points(grid: list, i: int, j: int, n: int, m: int) -> int:
    if grid[i + 1][j + 1] != 'A':
        return 0
    tl_br = grid[i][j] + 'A' + grid[i + 2][j + 2]
    if tl_br != 'SAM' and tl_br != 'MAS':
        return 0
    bl_tr = grid[i + 2][j] + 'A' + grid[i][j + 2]
    if bl_tr != 'SAM' and bl_tr != 'MAS':
        return 0
    return 1

grid = open('input2.txt').read().splitlines()
n = len(grid)
m = len(grid[0])

result = 0
for i in range(n - 2):
    for j in range(m - 2):
        result += starting_points(grid, i, j, n, m,)

print(result)
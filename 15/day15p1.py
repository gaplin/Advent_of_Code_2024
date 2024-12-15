def make_move(grid: list, n: int, i: int, j: int, di: int, dj: int) -> tuple:
    new_i, new_j = i + di, j + dj
    empty_i, empty_j = new_i, new_j
    while grid[empty_i][empty_j] not in '.#':
        empty_i, empty_j = empty_i + di, empty_j + dj
    if grid[empty_i][empty_j] != '.':
        return (i, j)
    while empty_i != new_i or empty_j != new_j:
        grid[empty_i][empty_j] = 'O'
        empty_i, empty_j = empty_i - di, empty_j - dj
    grid[new_i][new_j] = '@'
    grid[i][j] = '.'
    return (new_i, new_j)

grid, moves = open('input2.txt').read().strip().split('\n\n')
moves = ''.join(moves.split('\n'))
grid = grid.splitlines()
n = len(grid)
position = (0, 0)
for i in range(n):
    grid[i] = [x for x in grid[i]]
    for j in range(n):
        if grid[i][j] == '@':
            position = (i, j)

directions = {
    '>': (0, 1),
    'v': (1, 0),
    '<': (0, -1),
    '^': (-1, 0)
}

for move in moves:
    dir = directions[move]
    position = make_move(grid, n, *position, *dir)

result = 0
for i in range(1, n):
    for j in range(1, n):
        if grid[i][j] == 'O':
            result += 100 * i + j
print(result)
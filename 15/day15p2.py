def get_box(grid: list, i: int, j: int) -> tuple:
    if grid[i][j] == '[':
        return ((i, j), (i, j + 1))
    elif grid[i][j] == ']':
        return ((i, j - 1), (i, j))
    return None

def box_move_possible(grid: list, box: tuple, di: int, dj: int) -> bool:
    if di != 0:
        if grid[box[0][0] + di][box[0][1]] == '.' and grid[box[1][0] + di][box[1][1]] == '.':
            return True
        if grid[box[0][0] + di][box[0][1]] == '#' or grid[box[1][0] + di][box[1][1]] == '#':
            return False
        left_box = get_box(grid, box[0][0] + di, box[0][1])
        if left_box != None and box_move_possible(grid, left_box, di, dj) == False:
            return False
        right_box = get_box(grid, box[1][0] + di, box[1][1])
        if right_box != None and box_move_possible(grid, right_box, di, dj) == False:
            return False
        return True
    else:
        empty_i, empty_j = (box[0][0], box[0][1])
        while grid[empty_i][empty_j] not in '.#':
            empty_i, empty_j = empty_i + di, empty_j + dj
        if grid[empty_i][empty_j] == '#':
            return False
        return True
    
def make_box_move(grid: list, box: tuple, di: int, dj: int) -> bool:
    if di != 0:
        left_box = get_box(grid, box[0][0] + di, box[0][1])
        if left_box != None:
            make_box_move(grid, left_box, di, dj)
        right_box = get_box(grid, box[1][0] + di, box[1][1])
        if right_box != None:
            make_box_move(grid, right_box, di, dj)
        grid[box[0][0] + di][box[0][1]] = '['
        grid[box[1][0] + di][box[1][1]] = ']'
        grid[box[0][0]][box[0][1]] = '.'
        grid[box[1][0]][box[1][1]] = '.'
        return
    else:
        empty_i, empty_j = (box[0][0], box[0][1])
        while grid[empty_i][empty_j] != '.':
            empty_i, empty_j = empty_i + di, empty_j + dj
        hits = 0
        while hits != 2:
            if (empty_i == box[0][0] and empty_j == box[0][1]) or (empty_i == box[1][0] and empty_j == box[1][1]):
                hits += 1
            grid[empty_i][empty_j] = grid[empty_i - di][empty_j - dj]
            empty_i -= di
            empty_j -= dj

def make_box_move_if_possible(grid: list, i: int, j: int, di: int, dj: int) -> bool:
    box = get_box(grid, i, j)
    if box_move_possible(grid, box, di, dj):
        make_box_move(grid, box, di, dj)
        return True
    return False

def make_move(grid: list, i: int, j: int, di: int, dj: int) -> tuple:
    new_i, new_j = i + di, j + dj
    if (grid[new_i][new_j] in '[]' and make_box_move_if_possible(grid, new_i, new_j, di, dj) == True) or grid[new_i][new_j] == '.':
        grid[i][j] = '.'
        grid[new_i][new_j] = '@'
        return (new_i, new_j)
    
    return (i, j)


grid, moves = open('input2.txt').read().strip().split('\n\n')
moves = ''.join(moves.split('\n'))
grid = grid.splitlines()
n = len(grid)
position = (0, 0)
for i in range(n):
    changed_grid = []
    for j in range(n):
        if grid[i][j] == '#':
            changed_grid.append('#')
            changed_grid.append('#')
        elif grid[i][j] == '@':
            changed_grid.append('@')
            changed_grid.append('.')
        elif grid[i][j] == '.':
            changed_grid.append('.')
            changed_grid.append('.')
        elif grid[i][j] == 'O':
            changed_grid.append('[')
            changed_grid.append(']')
    grid[i] = changed_grid

m = len(grid[0])
for i in range(n):
    for j in range(m):
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
    position = make_move(grid, *position, *dir)

result = 0
for i in range(1, n):
    for j in range(2, m):
        if grid[i][j] == '[':
            result += 100 * i + j
print(result)
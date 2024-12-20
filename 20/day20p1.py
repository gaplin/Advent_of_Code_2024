grid = open('input2.txt').read().strip().splitlines()
n = len(grid)

start = None
end = None
for i in range(n):
    for j in range(n):
        if grid[i][j] == 'S':
            start = (i, j)
        elif grid[i][j] == 'E':
            end = (i, j)

distances = [[-1 for _ in range(n)] for _ in range(n)]
distances[start[0]][start[1]] = 0
position = start
path = []
while True:
    path.append(position)
    if position == end:
        break
    for next in [(position[0] + 1, position[1]), (position[0] - 1, position[1]), (position[0], position[1] - 1), (position[0], position[1] + 1)]:
        if grid[next[0]][next[1]] != '#' and distances[next[0]][next[1]] == -1:
            distances[next[0]][next[1]] = distances[position[0]][position[1]] + 1
            position = next
            break

result = 0
for i, j in path:
    for new_i, new_j in [(i - 2, j), (i - 1, j + 1), (i, j + 2), (i + 1, j + 1), (i + 2, j), (i + 1, j - 1), (i, j - 2), (i - 1, j - 1)]:
        if new_i < 0 or new_i >= n or new_j < 0 or new_j >= n or grid[new_i][new_j] == '#':
            continue
        if distances[new_i][new_j] - distances[i][j] >= 102:
            result += 1

print(result)
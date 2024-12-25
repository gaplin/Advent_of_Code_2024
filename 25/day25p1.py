grids = list(map(lambda x: x.splitlines(), open('input2.txt').read().strip().split('\n\n')))

keys = []
locks = []
n = len(grids[0])
m = len(grids[0][0])

for grid in grids:
    if grid[0][0] == '#': # lock
        all_heights = []
        for i in range(m):
            height = 0
            while grid[height + 1][i] == '#':
                height += 1
            all_heights.append(height)

        key = tuple(all_heights)
        locks.append(key)

    else: #key
        all_heights = []
        for i in range(m):
            height = 0
            last = n - 1
            while grid[last - 1][i] == '#':
                height += 1
                last -= 1
            all_heights.append(height)

        key = tuple(all_heights)
        keys.append(key)

result = 0
for lock in locks:
    for key in keys:
        target = tuple(map(lambda x: n - 2 - x, lock))
        for x, y in zip(key, target):
            if x > y:
                break
        else:
            result += 1

print(result)

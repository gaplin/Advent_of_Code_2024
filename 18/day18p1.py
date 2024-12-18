from queue import Queue

def shortest_distance(grid: list, n: int, start: tuple, end: tuple) -> int:
    visited = {start}
    q = Queue()
    q.put(start)
    distance = -1
    while q.empty() == False:
        distance += 1
        s = q.qsize()
        for _ in range(s):
            x, y = q.get()
            if (x, y) == end:
                return distance
            for new_x, new_y in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
                if new_x < 0 or new_x >= n or new_y < 0 or new_y >= n or (new_x, new_y) in visited or grid[new_y][new_x] != '.':
                    continue
                q.put((new_x, new_y))
                visited.add((new_x, new_y))
        
    return None

lines = open('input2.txt').read().splitlines()
n = 71
bytes = []
for line in lines:
    byte = line.split(',')
    byte = (int(byte[0]), int(byte[1]))
    bytes.append(byte)

grid = [['.' for x in range(n)] for _ in range(n)]
for x, y in bytes[:1024]:
    grid[y][x] = '#'

print(shortest_distance(grid, n, (0, 0), (n - 1, n - 1)))

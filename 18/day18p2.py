from queue import Queue

def path_exist(n: int, start: tuple, end: tuple, max_byte: int, bytes: list) -> bool:
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
                return True
            for new_x, new_y in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
                if new_x < 0 or new_x >= n or new_y < 0 or new_y >= n or (new_x, new_y) in visited or bytes[new_y][new_x] <= max_byte:
                    continue
                q.put((new_x, new_y))
                visited.add((new_x, new_y))
        
    return False

def first_blocking_byte(bytes: list, n: int) -> tuple:
    n_bytes = len(bytes)
    l = 0
    r = n_bytes - 1
    bytes_grid = [[n_bytes + 1 for _ in range(n)] for _ in range(n)]
    start = (0, 0)
    end = (n - 1, n - 1)
    for i in range(n_bytes):
        bytes_grid[bytes[i][1]][bytes[i][0]] = min(i, bytes_grid[bytes[i][1]][bytes[i][0]])
    while l < r:
        mid = (l + r) // 2
        if path_exist(n, start, end, mid, bytes_grid):
            l = mid + 1
        else:
            r = mid
    return bytes[l]

lines = open('input2.txt').read().splitlines()
n = 71
bytes = []
for line in lines:
    byte = line.split(',')
    byte = (int(byte[0]), int(byte[1]))
    bytes.append(byte)

print(','.join(map(str, first_blocking_byte(bytes, n))))
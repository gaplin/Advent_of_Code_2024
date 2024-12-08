grid = open('input2.txt').read().splitlines()
n = len(grid)
for i in range(n):
    grid[i] = [x for x in grid[i]]

antennas = {}
for i in range(n):
    for j in range(n):
        symbol = grid[i][j]
        if symbol != '.':
            if symbol not in antennas:
                antennas[symbol] = []
            antennas[symbol].append((i, j))

antinodes = set()
for _, group in antennas.items():
    m = len(group)
    antinodes.add(group[m - 1])
    for i in range(m - 1):
        A = group[i]
        antinodes.add(A)
        for j in range(i + 1, m):
            B = group[j]
            di = B[0] - A[0]
            dj = B[1] - A[1]

            for k in range(1, n):
                if 0 <= A[0] - k * di < n and 0 <= A[1] - k * dj < n:
                    antinodes.add((A[0] - k * di, A[1] - k * dj))
                else:
                    break
            
            for k in range(1, n):
                if 0 <= B[0] + k * di < n and 0 <= B[1] + k * dj < n:
                    antinodes.add((B[0] + k * di, B[1] + k * dj))
                else:
                    break

print(len(antinodes))
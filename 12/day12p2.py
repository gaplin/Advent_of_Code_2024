from queue import Queue

def get_num_of_edges(inside: set):
    all_points = set()
    directions = [(-0.5, -0.5), (0.5, -0.5), (0.5, 0.5), (-0.5, 0.5)]
    for i, j in inside:
        for di, dj in directions:
            all_points.add((i + di, j + dj))

    result = 0
    for i, j in all_points:
        region_hit = []
        hits = 0
        for di, dj in directions:
            new_i, new_j = i + di, j + dj
            hit = (new_i, new_j) in inside
            hits += hit
            region_hit.append(hit)
        if hits == 2:
            if region_hit == [True, False, True, False] or region_hit == [False, True, False, True]:
                result += 2
        elif hits < 4:
            result += 1

    return result

def get_fences_cost(grid: list, n: int, i: int, j: int, visited: set) -> int:
    q = Queue()
    q.put((i, j))
    area = 0
    visited.add((i, j))
    inside = set()
    while q.empty() == False:
        (i, j) = q.get()
        inside.add((i, j))
        area += 1
        for new_i, new_j in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
            if new_i < 0 or new_i >= n or new_j < 0 or new_j >= n or grid[new_i][new_j] != grid[i][j]:
                continue
            if (new_i, new_j) not in visited:
                visited.add((new_i, new_j))
                q.put((new_i, new_j))

    edges = get_num_of_edges(inside)
    return area * edges

grid = open('input2.txt').read().splitlines()
n = len(grid)

visited = set()
result = 0
for i in range(n):
    for j in range(n):
        if (i, j) not in visited:
            result += get_fences_cost(grid, n, i, j, visited)

print(result)

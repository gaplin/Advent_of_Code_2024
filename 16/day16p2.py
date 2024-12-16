from heapq import heappop, heappush
from queue import Queue

def get_marks(min_costs: dict, end_node: tuple, min_value: int):
    unique_nodes = set()
    visited = set()
    for direction in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        key = (end_node, direction)
        if key in min_costs and min_costs[key][0] == min_value:
            q = Queue()
            q.put(key)
            visited.add(key)
            while q.empty() == False:
                current = q.get()
                unique_nodes.add(current[0])
                nexts = min_costs[current][1:]
                for next in nexts:
                    if next not in visited:
                        visited.add(next)
                        q.put(next)
    
    return len(unique_nodes)

def get_min_distance(grid: list, start: tuple, end: tuple, turns: list, init_direction: tuple) -> int:
    q = [(0, start, init_direction)]
    min_costs = {(start, init_direction): [0]}
    while q:
        cost, position, direction = heappop(q)
        if cost != min_costs[(position, direction)][0]:
            continue
        if position == end:
            return get_marks(min_costs, position, cost)
        
        for turn, turn_cost in turns:
            new_direction = turn(direction)
            new_cost = cost + turn_cost + 1
            new_position = (position[0] + new_direction[0], position[1] + new_direction[1])
            if grid[new_position[0]][new_position[1]] != '#':
                key = (new_position, new_direction)
                if key not in min_costs or min_costs[key][0] > new_cost:
                    min_costs[key] = [new_cost, (position, direction)]
                    heappush(q, (new_cost, new_position, new_direction))
                elif min_costs[key][0] == new_cost:
                    min_costs[key].append((position, direction))

    return None

grid = open('input2.txt').read().strip().splitlines()
n = len(grid)

turns = [
    (lambda dir: dir, 0), # same direction  
    (lambda dir: (dir[1], -dir[0]), 1000), # left  
    (lambda dir: (-dir[1], dir[0]), 1000), # right  
    (lambda dir: (-dir[0], -dir[1]), 2000) # 180  
]

start = None
end = None
for i in range(n):
    for j in range(n):
        if grid[i][j] == 'E':
            end = (i, j)
        elif grid[i][j] == 'S':
            start = (i, j)

result = get_min_distance(grid, start, end, turns, (0, 1))
print(result)
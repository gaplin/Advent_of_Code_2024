from queue import Queue
import re
from functools import cache

def shortest_paths_in_grid(grid: list, n: int, m: int) -> map:
    directions = [(0, 1, '>'), (-1, 0, '^'), (0, -1, '<'), (1, 0, 'v')]
    result = {}
    for i in range(n):
        for j in range(m):
            if grid[i][j] == '#':
                continue

            q = Queue()
            visited = {(i, j): 0}
            q.put((i, j, 0, ''))
            while q.empty() == False:
                u = q.get()
                key = (grid[i][j], grid[u[0]][u[1]])
                if key not in result:
                    result[key] = []
                result[key].append(u[3] + 'A')
                for di, dj, symbol in directions:
                    new_i = u[0] + di
                    new_j = u[1] + dj
                    if new_i < 0 or new_i >= n or new_j < 0 or new_j >= m or grid[new_i][new_j] == '#':
                        continue
                    if (new_i, new_j) not in visited:
                        visited[(new_i, new_j)] = u[2] + 1
                    if visited[(new_i, new_j)] == u[2] + 1:
                        q.put((new_i, new_j, u[2] + 1, u[3] + symbol))
            
    return result

def shortest_path_in_numeric_keyboard() -> map:
    n = 4
    m = 3
    grid = [
        ['7', '8', '9'],
        ['4', '5', '6'],
        ['1', '2', '3'],
        ['#', '0', 'A']
    ]

    return shortest_paths_in_grid(grid, n, m)

def shortest_path_in_directional_keypad() -> map:
    n = 2
    m = 3
    grid = [
        ['#', '^', 'A'],
        ['<', 'v', '>']
    ]

    return shortest_paths_in_grid(grid, n, m)

def count_turns(path: str) -> int:
    turns = 0
    for prev, next in zip(path, path[1:]):
        if prev != next:
            turns += 1
    return turns

def opt_current_paths(paths: list) -> None:
    if len(paths) <= 1:
        return
    min_turns = count_turns(paths[0])
    for path in paths[1:]:
        turns = count_turns(path)
        if turns < min_turns:
            min_turns = turns
    new_paths = []
    for path in paths:
        if count_turns(path) == min_turns:
            new_paths.append(path)
    paths.clear()
    for path in new_paths:
        paths.append(path)


def opt_all_paths(all_paths: dict) -> None:
    for path in all_paths.values():
        opt_current_paths(path)

def get_shortest_rec_paths(a: str, b: str, directional_paths: map, depth: int) -> int:
    @cache
    def shortest_path_internal(a: str, b: str, depth: int) -> int:
        possible_shortest_paths = directional_paths[(a, b)]

        if depth == 0:
            return len(possible_shortest_paths[0])
        
        result = float('inf')
        
        for possible_path in possible_shortest_paths:
            current_result = 0
            for x, y in zip('A' + possible_path, possible_path):
                current_result += shortest_path_internal(x, y, depth - 1)
            result = min(result, current_result)
        return result
        
    return shortest_path_internal(a, b, depth)



def get_shortest_path(code: str, numeric_paths: map, directional_paths: map) -> str:
    position = 'A'
    result = None
    possible_shortest_paths = ['']
    for symbol in code:
        possible_paths = numeric_paths[(position, symbol)]
        position = symbol
        new_paths = []
        for current_path in possible_shortest_paths:
            for partial_path in possible_paths:
                new_paths.append(current_path + partial_path)
        possible_shortest_paths = new_paths

    result = float("inf")
    for possible_path in possible_shortest_paths:
        current_result = 0
        for x, y in zip('A' + possible_path, possible_path):
            current_result += get_shortest_rec_paths(x, y, directional_paths, 24)
        result = min(current_result, result)
    return result

    
numeric_shortest_paths = shortest_path_in_numeric_keyboard()
directional_shortest_paths = shortest_path_in_directional_keypad()
opt_all_paths(numeric_shortest_paths)
opt_all_paths(directional_shortest_paths)

codes = open('input2.txt').read().strip().splitlines()

result = 0
for code in codes:
    num_value = int(re.findall(r'\d+', code)[0])
    shortest_path = get_shortest_path(code, numeric_shortest_paths, directional_shortest_paths)
    result += num_value * shortest_path

print(result)
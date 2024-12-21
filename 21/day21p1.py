from queue import Queue
import re

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
                result[key].append(u[3])
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

def get_shortest_rec_paths(code: str, directional_paths: map, depth: int) -> str:
    position = 'A'
    possible_shortest_paths = ['']
    for symbol in code:
        possible_paths = directional_paths[(position, symbol)]
        position = symbol
        new_paths = []
        for current_path in possible_shortest_paths:
            for partial_path in possible_paths:
                new_paths.append(current_path + partial_path + 'A')
        possible_shortest_paths = new_paths

    if depth == 0:
        return possible_shortest_paths[0]

    if depth > 0:
        result = ''
        for possible_path in possible_shortest_paths:
            rec_path = get_shortest_rec_paths(possible_path, directional_paths, depth - 1)
            if result == '':
                result = rec_path
            elif len(result) > len(rec_path):
                result = rec_path
        return result



def get_shortest_path(code: str, numeric_paths: map, directional_paths: map) -> str:
    position = 'A'
    result = ''
    possible_shortest_paths = ['']
    for symbol in code:
        possible_paths = numeric_paths[(position, symbol)]
        position = symbol
        new_paths = []
        for current_path in possible_shortest_paths:
            for partial_path in possible_paths:
                new_paths.append(current_path + partial_path + 'A')
        possible_shortest_paths = new_paths


    for possible_path in possible_shortest_paths:
        rec_path = get_shortest_rec_paths(possible_path, directional_paths, 1)
        if result == '':
            result = rec_path
        elif len(result) > len(rec_path):
            result = rec_path
    return result

    
numeric_shortest_paths = shortest_path_in_numeric_keyboard()
directional_shortest_paths = shortest_path_in_directional_keypad()

codes = open('input2.txt').read().strip().splitlines()

result = 0
for code in codes:
    num_value = int(re.findall(r'\d+', code)[0])
    shortest_path = get_shortest_path(code, numeric_shortest_paths, directional_shortest_paths)
    result += num_value * len(shortest_path)

print(result)
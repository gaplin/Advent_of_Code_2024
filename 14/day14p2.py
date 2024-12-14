import re
from queue import Queue

def largest_connected_component(robots: set, width: int, height: int) -> int:
    visited = set()
    result = 0
    for x, y in robots:
        if (x, y) in visited:
            continue
        q = Queue()
        q.put((x, y))
        visited.add((x, y))
        current_size = 0
        while q.empty() == False:
            current_size += 1
            x, y = q.get()
            for new_x, new_y in [((x + 1) % width, y), ((x - 1) % width, y), (x, (y + 1) % height), (x, (y - 1) % height)]:
                if (new_x, new_y) in robots and (new_x, new_y) not in visited:
                    visited.add((new_x, new_y))
                    q.put((new_x, new_y))
        result = max(result, current_size)

    return result

def print_grid(robots: set, width: int, height: int):
    for i in range(height):
        for j in range(width):
            if (i, j) in robots:
                print('#', end='')
            else:
                print('.', end='')
        print('')

width = 101
height = 103
input = open('input2.txt').read().splitlines()
robots = []

for line in input:
    robots.append(tuple(int(x) for x in re.findall(r'[-0-9]+', line)))

mid_horizontal = height // 2
mid_vertical = width // 2

max_time = 0
max_connected_component = 0
snapshot = set()
for time in range(width * height):
    all_places = set()
    new_robots = []
    for x, y, dx, dy in robots:
        x = (x + dx) % width
        y = (y + dy) % height
        all_places.add((x, y))
        new_robots.append((x, y, dx, dy))
    
    largest_connected_size = largest_connected_component(all_places, width, height)
    if largest_connected_size > max_connected_component:
        max_connected_component = largest_connected_size
        max_time = time + 1
        snapshot = all_places
    robots = new_robots

print(max_time)
print_grid(snapshot, width, height)
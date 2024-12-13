def get_min_cost(target: tuple, A: tuple, B: tuple) -> int:
    for i in range(target[0] + 1):
        new_target = (target[0] - i * B[0], target[1] - i * B[1])
        if new_target == (0, 0):
            return i
        if new_target[0] < 0 or new_target[1] < 0:
            return None
        if new_target[0] % A[0] != 0 or new_target[1] % A[1] != 0 or new_target[0] // A[0] != new_target[1] // A[1]:
            continue
        return i + 3 * new_target[0] // A[0]

import re

input = open('input2.txt').read().strip().split('\n\n')

result = 0
for game in input:
    lines = game.splitlines()
    A = tuple(int(x) for x in re.findall(r'\d+', lines[0]))
    B = tuple(int(x) for x in re.findall(r'\d+', lines[1]))
    target = tuple(int(x) for x in re.findall(r'\d+', lines[2]))
    min_cost = get_min_cost(target, A, B)
    if min_cost != None:
        result += min_cost

print(result)
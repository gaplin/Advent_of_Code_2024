def get_min_cost(target: tuple, A: tuple, B: tuple) -> int:
    FA = (target[0] * B[1] - target[1] * B[0]) / (A[0] * B[1] - A[1] * B[0])
    FB = (target[0] - A[0] * FA) / B[0]
    if FA % 1 == 0 and FB % 1 == 0:
        return int(3 * FA + FB)
    return None

import re

input = open('input2.txt').read().strip().split('\n\n')

result = 0
for game in input:
    lines = game.splitlines()
    A = tuple(int(x) for x in re.findall(r'\d+', lines[0]))
    B = tuple(int(x) for x in re.findall(r'\d+', lines[1]))
    target = tuple(int(x) + 10000000000000 for x in re.findall(r'\d+', lines[2]))
    min_cost = get_min_cost(target, A, B)
    if min_cost != None:
        result += min_cost

print(result)
import re
from functools import reduce

input = open('input2.txt').read().strip()

muls = re.findall(r'mul\(\d{1,3},\d{1,3}\)', input)

result = reduce(lambda current, next: current + next[0] * next[1], map(lambda x: [int(y) for y in re.findall(r'\d+', x)], muls), 0)
print(result)
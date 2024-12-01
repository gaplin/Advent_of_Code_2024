import re
import collections

lines = open('input2.txt').read().splitlines()

first_column = []
second_column = collections.defaultdict(int)
for line in lines:
    lst = [int(x) for x in re.findall(r'\d+', line)]

    first_column.append(lst[0])
    second_column[lst[1]] += 1

result = 0
for x in first_column:
    result += x * second_column[x]

print(result)
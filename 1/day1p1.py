import re

lines = open('input2.txt').read().splitlines()

first_column = []
second_column = []
for line in lines:
    lst = [int(x) for x in re.findall(r'\d+', line)]

    first_column.append(lst[0])
    second_column.append(lst[1])

first_column.sort()
second_column.sort()

result = 0
for x, y in zip(first_column, second_column):
    result += abs(x - y)

print(result)
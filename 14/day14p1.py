import re

width = 101
height = 103
input = open('input2.txt').read().splitlines()
robots = []

for line in input:
    robots.append(tuple(int(x) for x in re.findall(r'[-0-9]+', line)))


for _ in range(100):
    new_robots = []
    for x, y, dx, dy in robots:
        new_robots.append(((x + dx) % width, (y + dy) % height, dx, dy))

    robots = new_robots

quadrons = [0, 0, 0, 0]
mid_horizontal = height // 2
mid_vertical = width // 2
for x, y, _, _ in robots:
    if x == mid_vertical or y == mid_horizontal:
        continue
    if x < mid_vertical and y < mid_horizontal:
        quadrons[0] += 1
    elif x > mid_vertical and y < mid_horizontal:
        quadrons[1] += 1
    elif x < mid_vertical and y > mid_horizontal:
        quadrons[2] += 1
    else :
        quadrons[3] += 1

print(quadrons[0] * quadrons[1] * quadrons[2] * quadrons[3])
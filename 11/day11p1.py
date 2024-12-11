from collections import deque

nums = [int(x) for x in open('input2.txt').read().strip().split(' ')]

q = deque(nums)

for _ in range(25):
    s = len(q)
    for _ in range(s):
        stone = q.popleft()
        if stone == 0:
            q.append(1)
        else:
            stone_str = str(stone)
            l = len(stone_str)
            if l % 2 == 0:
                half = l // 2
                q.append(int(stone_str[:half]))
                q.append(int(stone_str[half:]))
            else:
                q.append(stone * 2024)

print(len(q))
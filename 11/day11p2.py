from collections import deque

def count_stones(stone: int, time: int, cache: dict) -> int:
    if time == 0:
        return 1
    
    key = (stone, time)
    if key in cache:
        return cache[key]
    
    result = 0
    if stone == 0:
        result = count_stones(1, time - 1, cache)
    else:
        stone_str = str(stone)
        l = len(stone_str)
        if l % 2 == 0:
            half = l // 2
            left = int(stone_str[:half])
            right = int(stone_str[half:])
            result = count_stones(left, time - 1, cache) + count_stones(right, time - 1, cache)
        else:
            result = count_stones(stone * 2024, time - 1, cache)
    cache[key] = result
    return result 

nums = [int(x) for x in open('input2.txt').read().strip().split(' ')]

result = 0
for num in nums:
    result += count_stones(num, 75, {})

print(result)
import re

lines = open('input2.txt').read().splitlines()

result = 0
for report in lines:
    nums = [int(x) for x in re.findall(r'\d+', report)]
    diff = nums[1] - nums[0]
    if diff == 0:
        continue
    for i in range(1, len(nums)):
        current_diff = nums[i] - nums[i - 1]
        if (diff < 0 and current_diff >= 0) or (diff > 0 and current_diff <= 0) or abs(current_diff) > 3:
            break
    else:
        result += 1


print(result)
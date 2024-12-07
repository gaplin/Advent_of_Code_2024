input = open('input2.txt').read().splitlines()

def possible_nums(target: int, nums: list) -> bool:
    if len(nums) == 1:
        return target == nums[0]
    if target > nums[-1] and possible_nums(target - nums[-1], nums[:-1]):
        return True
    if target % nums[-1] == 0 and possible_nums(target // nums[-1], nums[:-1]):
        return True
    if str(target).endswith(str(nums[-1])) and possible_nums(int(str(target)[:-len(str(nums[-1]))]), nums[:-1]):
        return True
    return False

result = 0
for line in input:
    target, rest = line.split(': ')
    target = int(target)
    nums = [int(x) for x in rest.split(' ')]
    if possible_nums(target, nums):
        result += target

print(result)


input = open('input2.txt').read().splitlines()

result = 0
for line in input:
    target, rest = line.split(': ')
    target = int(target)
    nums = [int(x) for x in rest.split(' ')]
    n = len(nums)
    iters = 3 ** (n - 1)
    for i in range(iters):
        equation_result = nums[0]
        for j in range(1, n):
            mod = i % 3
            if mod == 0:
                equation_result *= nums[j]
            elif mod == 1:
                equation_result += nums[j]
            else:
                equation_result = int(str(equation_result) + str(nums[j]))
            i //= 3
        if equation_result == target:
            result += target
            break

print(result)


def mix(num: int, secret: int) -> int:
    return num ^ secret

def prune(secret: int) -> int:
    mask = (1 << 24) - 1
    return secret & mask

def evolve(secret: int) -> int:
    num = secret << 6
    secret = mix(num, secret)
    secret = prune(secret)

    num = secret >> 5
    secret = mix(num, secret)
    secret = prune(secret)

    num = secret << 11
    secret = mix(num, secret)
    secret = prune(secret)

    return secret

def get_bananas(secret: int, count: int) -> list:
    result = [0] * (count + 1)
    result[0] = secret
    for i in range(1, count + 1):
        result[i] = evolve(result[i - 1])
    for i in range(count + 1):
        result[i] %= 10
    return result

def fill_changes(nums: list, n: int, candidates: dict) -> None:
    visited = set()
    for i in range(4, n):
        diffs = []
        for j in range(i - 3, i + 1):
            diffs.append(nums[j] - nums[j - 1])
        key = tuple(diffs)
        if key not in visited:
            if key not in candidates:
                candidates[key] = nums[i]
            else:
                candidates[key] += nums[i]
            visited.add(key)

secrets = list(map(int, open('input2.txt').read().strip().splitlines()))

candidates = {}
for secret in secrets:
    bananas = get_bananas(secret, 2000)
    fill_changes(bananas, 2001, candidates)

print(max(candidates.values()))
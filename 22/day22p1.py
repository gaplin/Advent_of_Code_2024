def mix(num: int, secret: int) -> int:
    return num ^ secret

def prune(secret: int) -> int:
    mod = 16777216
    return secret % mod

def evolve(secret: int) -> int:
    num = secret * 64
    secret = mix(num, secret)
    secret = prune(secret)

    num = secret // 32
    secret = mix(num, secret)
    secret = prune(secret)

    num = secret * 2048
    secret = mix(num, secret)
    secret = prune(secret)

    return secret

secrets = list(map(int, open('input2.txt').read().strip().splitlines()))

n = len(secrets)
for i in range(n):
    for _ in range(2000):
        secrets[i] = evolve(secrets[i])

print(sum(secrets))
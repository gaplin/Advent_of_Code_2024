def possible_pattern(towels: set, pattern: str) -> bool:
    if pattern == '':
        return True
    for i in range(len(pattern), 0, -1):
        if pattern[:i] in towels:
            if possible_pattern(towels, pattern[i:]):
                return True
            
    return False

towels, patterns = open('input2.txt').read().strip().split('\n\n')
towels = towels.split(', ')
patterns = patterns.splitlines()

towels = set(towels)

result = 0
for pattern in patterns:
    if possible_pattern(towels, pattern):
        result += 1

print(result)
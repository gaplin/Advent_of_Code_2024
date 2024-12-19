from functools import lru_cache

def possible_patterns(towels: set, pattern: str) -> bool:
    @lru_cache
    def possible_patterns_internal(pattern: str) -> bool:
        if pattern == '':
            return 1
        all_ways = 0
        for i in range(len(pattern), 0, -1):
            if pattern[:i] in towels:
                all_ways += possible_patterns_internal(pattern[i:])
                
        return all_ways
    
    return possible_patterns_internal(pattern)

towels, patterns = open('input2.txt').read().strip().split('\n\n')
towels = towels.split(', ')
patterns = patterns.splitlines()

towels = set(towels)

result = 0
for pattern in patterns:
    result += possible_patterns(towels, pattern)

print(result)
lines = open('input2.txt').read().splitlines()

n_lines = len(lines)
n = 0
pairs = set()
while lines[n] != '':
    u, v = [int(x) for x in lines[n].split('|')]
    pairs.add((u, v))
    n += 1
n += 1
cases = []
while n < n_lines:
    cases.append([int(x) for x in lines[n].split(',')])
    n += 1

result = 0
for case in cases:
    m = len(case)
    valid = True
    for i in range(m - 1):
        u = case[i]
        for j in range(i + 1, m):
            v = case[j]
            if (v, u) in pairs:
                valid = False
                break
        if valid == False:
            break
    if valid == False:
        new_case = []
        for _ in range(m):
            k = len(case)
            idx_to_add = 0
            for i in range(k):
                before = 0
                for j in range(k):
                    if i == j:
                        continue
                    if (case[i], case[j]) in pairs:
                        before += 1
                if before == 0:
                    idx_to_add = i
                    break
            item = case[idx_to_add]
            case.pop(idx_to_add)
            new_case.insert(0, item)
        result += new_case[m // 2]
        
print(result)
edges = set(map(tuple, map(lambda x : x.split('-'), open('input2.txt').read().strip().splitlines())))
computers = set()
for u, v in edges:
    computers.add(u)
    computers.add(v)

computers = list(computers)
n = len(computers)
result = 0
for i in range(2, n):
    u = computers[i]
    for j in range(1, i):
        v = computers[j]
        if (u, v) not in edges and (v, u) not in edges:
            continue
        for k in range(0, j):
            w = computers[k]
            if (u[0] != 't' and v[0] != 't' and w[0] != 't'):
                continue
            if (u, w) not in edges and (w, u) not in edges:
                continue
            if (v, w) not in edges and (w, v) not in edges:
                continue
            result += 1

print(result)
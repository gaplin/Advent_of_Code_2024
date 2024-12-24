initial_values, connections = open('input2.txt').read().strip().split('\n\n')

initial_values = initial_values.splitlines()
connections = connections.splitlines()

values = {}
for value in initial_values:
    node, value = value.split(': ')
    value = int(value)
    values[node] = value

new_connections = []
for connection in connections:
    source, target = connection.split(' -> ')
    u, op, v = source.split(' ')
    new_connections.append((u, op, v, target))

connections = new_connections

ops = {
    'AND': lambda x, y : x & y,
    'OR': lambda x, y : x | y,
    'XOR': lambda x, y : x ^ y
}
while True:
    new_connections = []
    any_op = False
    for u, op, v, target in connections:
        if u not in values or v not in values:
            new_connections.append((u, op, v, target))
            continue
        res = ops[op](values[u], values[v])
        values[target] = res
        any_op = True
    connections = new_connections
    if any_op == False:
        break

digits = []
for key, value in values.items():
    if key[0] == 'z':
        which_digits = int(key[1:])
        digits.append((which_digits, value))

digits.sort()
result = 0
p = 1
for _, digit in digits:
    result += p * digit
    p <<= 1

print(result)
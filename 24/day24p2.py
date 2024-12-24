def get_wire(char: str, num: int) -> str:
    return char + str(num).rjust(2, '0')

def get_first_wrong_idx(formulas: dict) -> int:
    for i in range(0, 100):
        wire = get_wire('z', i)
        if wire not in formulas:
            return i
        if verify_bit(i, formulas) == False:
            return i
        
def verify_bit(num: int, formulas: dict) -> bool:
    u, op, v = formulas[get_wire('z', num)]
    if op != 'XOR':
        return False
    if num == 0:
        return u == 'x00' and v == 'y00'
    return (verify_xor(formulas, u, num) and verify_carry_bit(formulas, v, num)) \
          or (verify_xor(formulas, v, num) and verify_carry_bit(formulas, u, num))

def verify_xor(formulas: dict, wire: str, num: int) -> bool:
    if wire not in formulas:
        return False
    u, op, v = formulas[wire]
    if op != 'XOR':
        return False
    return u == get_wire('x', num) and v == get_wire('y', num)

def verify_carry_bit(formulas: dict, wire: str, num: int) -> bool:
    if wire not in formulas:
        return False
    u, op, v = formulas[wire]
    if num == 1:
        return op == 'AND' and u == 'x00' and v == 'y00'
    if op != 'OR':
        return False
    return (verify_direct_carry(formulas, u, num - 1) and verify_recarry(formulas, v, num - 1)) \
        or (verify_direct_carry(formulas, v, num - 1) and verify_recarry(formulas, u, num - 1))

def verify_direct_carry(formulas: dict, wire: str, num: int) -> bool:
    if wire not in formulas:
        return False
    u, op, v = formulas[wire]
    if op != 'AND':
        return False
    return u == get_wire('x', num) and v == get_wire('y', num)

def verify_recarry(formulas: dict, wire: str, num: int) -> bool:
    if wire not in formulas:
        return False
    u, op, v = formulas[wire]
    if op != 'AND':
        return False
    return (verify_xor(formulas, u, num) and verify_carry_bit(formulas, v, num)) \
        or (verify_xor(formulas, v, num) and verify_carry_bit(formulas, u, num))

connections = open('input2.txt').read().strip().split('\n\n')[1]
connections = connections.splitlines()

formulas = {}
for connection in connections:
    source, target = connection.split(' -> ')
    u, op, v = source.split(' ')
    formulas[target] = (u, op, v)
    if u > v:
        formulas[target] = (v, op, u)

swaps = []
for _ in range(4):
    first_invalid = get_first_wrong_idx(formulas)
    for x in formulas.keys():
        for y in formulas.keys():
            if x == y:
                continue
            formulas[x], formulas[y] = formulas[y], formulas[x]
            if first_invalid < get_first_wrong_idx(formulas):
                swaps.append(x)
                swaps.append(y)
                break
            formulas[x], formulas[y] = formulas[y], formulas[x]
        else:
            continue
        break

print(','.join(sorted(swaps)))
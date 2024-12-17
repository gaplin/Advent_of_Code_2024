def get_combo_value(registers: list, operand: int) -> int:
    if operand <= 3:
        return operand
    if operand == 7:
        raise Exception('7 passed to combo')
    return registers[operand - 4]

def adv(registers: list, operand: int, ip: list) -> None:
    numerator = registers[0]
    denominator = 2 ** get_combo_value(registers, operand)
    registers[0] = numerator // denominator
    ip[0] += 2

def bxl(registers: list, operand: int, ip: list) -> None:
    registers[1] ^= operand
    ip[0] += 2

def bst(registers: list, operand: int, ip: list) -> None:
    registers[1] = get_combo_value(registers, operand) % 8
    ip[0] += 2

def jnz(registers: list, operand: int, ip: list) -> None:
    if registers[0] == 0:
        ip[0] += 2
    else :
        ip[0] = operand

def bxc(registers: list, operand: int, ip: list) -> None:
    registers[1] ^= registers[2]
    ip[0] += 2

def out(registers: list, operand: int, ip: list) -> int:
    value = get_combo_value(registers, operand) % 8
    ip[0] += 2
    return value

def bdv(registers: list, operand: int, ip: list) -> None:
    numerator = registers[0]
    denominator = 2 ** get_combo_value(registers, operand)
    registers[1] = numerator // denominator
    ip[0] += 2

def cdv(registers: list, operand: int, ip: list) -> None:
    numerator = registers[0]
    denominator = 2 ** get_combo_value(registers, operand)
    registers[2] = numerator // denominator
    ip[0] += 2

def apply_instruction(registers: list, program: list, ip: list):
    instructions = {
        0: adv,
        1: bxl,
        2: bst,
        3: jnz,
        4: bxc,
        5: out,
        6: bdv,
        7: cdv
    }
    opcode = program[ip[0]]
    operand = program[ip[0] + 1]
    result = instructions[opcode](registers, operand, ip)
    return result

registers, program = open('input2.txt').read().split('\n\n')
registers = registers.splitlines()
registers = [int(x.split(': ')[1]) for x in registers]
program = list(map(int, program.split(': ')[1].split(',')))

ip = [0]
n = len(program)
result = []
while 0 <= ip[0] < n:
    op_result = apply_instruction(registers, program, ip)
    if op_result != None:
        result.append(op_result)

print(','.join(map(str, result)))
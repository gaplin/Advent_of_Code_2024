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

def get_first_output(registers: list, program: list) -> int:
    ip = [0]
    while True:
        op_result = apply_instruction(registers, program, ip)
        if op_result != None:
            return op_result

def get_result(program: list, to_cover: list, result: int) -> int:
    if to_cover == []:
        return result
    for i in range(8):
        a = result << 3 | i
        if get_first_output([a, 0, 0], program) == to_cover[-1]:
            rec_step = get_result(program, to_cover[:-1], a)
            if rec_step != None:
                return rec_step

registers, program = open('input2.txt').read().split('\n\n')
program = list(map(int, program.split(': ')[1].split(',')))

print(get_result(program, list(program), 0))
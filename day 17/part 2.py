a = 53437164
b = 0
c = 0
program = 2,4,1,7,7,5,4,1,1,4,5,5,0,3,3,0

def get_combo_operand(operand, a, b, c):
    match operand:
        case 4: return a
        case 5: return b
        case 6: return c
    return operand

def perform_program(a, b, c, program):
    pointer = 0
    output = ""
    while pointer < len(program)-1:
        opcode, operand = program[pointer], program[pointer+1]
        combo_operand = get_combo_operand(operand, a, b, c)
        pointer += 2
        match opcode:
            case 0:
                a //= 2**combo_operand
            case 1:
                b ^= operand
            case 2:
                b = combo_operand % 8
            case 3:
                if a != 0:
                    pointer = operand
            case 4:
                b ^= c
            case 5:
                output += str(combo_operand % 8) + ", "
            case 6:
                b = a // (2**combo_operand)
            case 7:
                c = a // (2**combo_operand)
    return output[:-2]


for a in range(99999, 999999999):
    if perform_program(a, b, c, program) == str(program)[1:-1]:
        break

print(a)

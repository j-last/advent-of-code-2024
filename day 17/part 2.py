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

from time import sleep
# after some investigation, the length of the output program is to do with powers of 8
# if 'a' is between 8^2 and 8^3, it will output 3 values
# we need it to output len(program) = 16 values
# so we need a between 8^15 & 8^16
# this is still too many values to check though
# only the ones from the number below end in 0s though
for a in range(109549449117696, 109550657077248):
    if perform_program(a, b, c, program) == str(program)[1:-1]:
        print(a)
        break

print("end")

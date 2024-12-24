
# input data --------------------------------------------------------

with open(r"day 24\wires.txt", "r") as f:
    wires_file = f.read().split("\n")

with open(r"day 24\gates.txt", "r") as f:
    gates_file = f.read().split("\n")

# -------------------------------------------------------------------

# wires file -> dictionary ------------------------------------------

wires = {}
for line in wires_file:
    key, value = line.split(": ")
    wires[key] = bool(int(value))


# -------------------------------------------------------------------

def perform_logic(wires, operand1, operator, operand2, output_wire):
    """Performs the operator on the boolean operands.
    Appends the dictionary 'wires' with the 'output_wire:result' key value pair.
    """
    operand1 = wires[operand1]
    operand2 = wires[operand2]

    if operator == "AND":
        wires[output_wire] = operand1 and operand2
    elif operator == "OR":
        wires[output_wire] = operand1 or operand2
    elif operator == "XOR":
        wires[output_wire] = operand1 ^ operand2
    
    return wires


def get_binary(letter):
    """Gets the binary string specified by all wires starting with a certain letter.
    """
    output = ""
    for i in range(100):
        # converts to a string and adds preceding zeros to make 2 digits
        letter_wire = letter + "0"*(2-len(str(i))) + str(i)
        if wires.get(letter_wire) is None:
            break
        output = str(int(wires[letter_wire])) + output
    return output


def to_denary(binary):
    """Converts a binary string to a denary number.
    """
    denary = 0
    multiplier = 1
    for digit in binary[::-1]:
        digit = int(digit)
        denary += digit * multiplier
        multiplier *= 2
    return denary

# -------------------------------------------------------------------

x_num = to_denary(get_binary("x"))
y_num = to_denary(get_binary("y"))
expected_result = x_num + y_num
from random import randint
result = None
while result != expected_result:
    gates = gates_file.copy()
    swaps = []
    for i in range(4):
        swap1, swap2 = randint(0, len(gates)-1), randint(0, len(gates)-1)
        gates[swap1], gates[swap2] = gates[swap1][:-3] + gates[swap2][-3:], gates[swap2][:-3] + gates[swap1][-3:]
        swaps.append((gates[swap2][-3:], gates[swap1][-3:]))

    # works through the gates file and performs all operations that can be
    # performed until all operationa have been performed (gates_file becomes empty)
    
    while gates:
        for line in gates[::-1]:
            operand1, operator, operand2, _, output_wire = line.split(" ")

            if wires.get(operand1) is None or wires.get(operand2) is None:
                continue

            wires = perform_logic(wires, operand1, operator, operand2, output_wire)
            gates.remove(line)

print(swaps)

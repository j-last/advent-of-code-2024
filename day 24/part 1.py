
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


# works through the gates file and performs all operations that can be
# performed until all operationa have been performed (gates_file becomes empty)
while gates_file:
    for line in gates_file[::-1]:
        operand1, operator, operand2, _, output_wire = line.split(" ")

        if wires.get(operand1) is None or wires.get(operand2) is None:
            continue

        wires = perform_logic(wires, operand1, operator, operand2, output_wire)
        gates_file.remove(line)


# gets the value of all 'z' gates and adds their values to a binary string ('output')
output = ""
for i in range(100):
    # converts to a string and adds preceding zeros to make 2 digits
    z_wire = "z" + "0"*(2-len(str(i))) + str(i)
    if wires.get(z_wire) is None:
        break
    output = str(int(wires[z_wire])) + output


# converts this 'output' binary string to a denary integer
result = 0
multiplier = 1
for digit in output[::-1]:
    digit = int(digit)
    result += digit * multiplier
    multiplier *= 2

# this is the answer to the puzzle
print(result)

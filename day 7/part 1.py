
def den_to_bin(den, length):
    binary = str(bin(den))[2:]
    binary = "0" * (length - len(binary)) + binary
    return binary

def can_be_true(value, original_operands):
    for i in range(2 ** (len(original_operands)-1)):
        binary = den_to_bin(i, len(original_operands) - 1)

        operands = original_operands.copy()
        total = operands.pop(0)
        for digit in binary:
            match digit:
                case "0": total += operands.pop(0)
                case "1": total *= operands.pop(0)  

        if total == value:
            return True  
    return False

with open(r"day 7\input.txt", "r") as f:
    input = f.read()
    input = input.split("\n")

total = 0

for line in input:
    line = line.split(": ")
    line[0] = int(line[0])
    line[1] = list(map(int, line[1].split(" ")))

    if can_be_true(line[0], line[1]):
        total += line[0]

print(total)
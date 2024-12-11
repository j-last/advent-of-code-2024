
def can_be_true(value, operands):
    def inner_func(value, current_total, operands):
        if len(operands) == 0:
            if current_total == value:
                # if the end of the list i sreached and that combination of operators
                # produces the value, then return that the value can be produced,
                # and exit the recursion
                return True
            # otherwise this is not the right combination of operators
            # (go back and try other combinations)
            else: return False
        # applies each operator and checks permutations of the rest of the list
        if inner_func(value, current_total + operands[0], operands[1:]):
            return True
        elif inner_func(value, current_total * operands[0], operands[1:]):
            return True
        elif inner_func(value, int(str(current_total) + str(operands[0])), operands[1:]):
            return True
    # after the recursive function has terminated,
    # it either has found a way to do it (True) or not (False)
    return inner_func(value, 0, operands)

with open(r"day 7\input.txt", "r") as f:
    input = f.read()
    input = input.split("\n")

total = 0

for i, line in enumerate(input):
    line = line.split(": ")
    line[0] = int(line[0])
    line[1] = list(map(int, line[1].split(" ")))

    if can_be_true(line[0], line[1]):
        total += line[0]

print(total)


# PART 1 -------------------------
def check_correct_update(rules, update):
    for i in range(len(update)):
        for j, num in enumerate(update[i:]):
            # checks each number to see if it should be after a number that is
            # currrently before
            if rules.get(num) is not None and update[i] in rules[num]:
                return 0  # if so the order is wrong so return 0
    # if the order is valid, return the middle page num.
    return update[len(update) // 2]

# PART 2 ----------------------
def check_incorrect_update(rules, update):
    for i in range(len(update)):
        for j, num in enumerate(update[i:]):
            # checks each number to see if it should be after a number that is
            # currrently before
            if rules.get(num) is not None and update[i] in rules[num]:
                # if so the order is wrong, so change the order
                return change_update(rules, update, i, i+j)
    # if the order is valid OR has been corrected, return the middle page num.
    return update[len(update) // 2]

def change_update(rules, update, index1, index2):
    # swaps the incorrectly ordered values around and tries again
    update[index1], update[index2] = update[index2], update[index1]
    # (may call back and forth a few times before fully correcting the order)
    return check_incorrect_update(rules, update)

# SETUP ----------------------------
def convert_to_dict(input:str):
    output = {}
    for rule in input:
        rule = rule.split("|")
        if output.get(int(rule[0])) is None:
            output[int(rule[0])] = [int(rule[1])]
        else:
            output[int(rule[0])].append(int(rule[1]))
    return output

def convert_to_list(input):
    output = []
    for update in input:
        output.append(list(map(int, update.split(","))))
    return output

with open(r"day 5t\ordering_rules.txt", "r") as f:
    ordering = f.readlines()
with open(r"day 5\updates.txt", "r") as f:
    updates = f.readlines()

ordering = convert_to_dict(ordering)
updates = convert_to_list(updates)

# BOTH PARTS -------------------------
def check_ordering(rules, updates):
    total1 = 0
    total2 = 0
    for update in updates:
        total1 += check_correct_update(rules, update)
        total2 += check_incorrect_update(rules, update)
    # total2 conatins the sum of the middle pages of the correct orders and the
    # ones that have been changed, so subtract the originally correct sum to
    # get just the changed ones sum
    total2 -= total1
    return total1, total2

print(
    check_ordering(ordering, updates)
)

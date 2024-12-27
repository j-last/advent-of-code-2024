with open(r"day 25\input.txt", "r") as f:
    in_file = f.read().split("\n")


keys = []
locks = []
for line_num, startline in enumerate(in_file[::8]):
    line_num *= 8
    lockey = in_file[line_num:line_num+7]

    to_add = []
    for i in range(5):
        total = -1
        for line in lockey:
            if line[i] == "#":
                total += 1
        to_add.append(total)
    if startline == "#####":
        locks.append(to_add)
    else:
        keys.append(to_add)

fit = 0
for lock in locks:
    for key in keys:
        for num1, num2 in zip(lock, key):
            if num1 + num2 >= 6:
                break
        else:
            fit += 1
print(fit)

        
            
                

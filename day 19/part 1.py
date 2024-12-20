
with open(r"day 19\towels.txt", "r") as f:
    towels = f.read().split(", ")

with open(r"day 19\designs.txt", "r") as f:
    designs = f.read().split("\n")

max_stripes = 0
for towl in towels:
    max_stripes = max(max_stripes, len(towl))

# -------------------------------------------------------------------
doesnt_work = []
def check_design(design, towels):
    if design == "":
        return True
    elif design in doesnt_work:
        return False
    
    for i in range(max_stripes, -1, -1):
        if design[:i] in towels:
            if check_design(design[i:], towels):
                return True
    doesnt_work.append(design)
    return False


total = 0
for design in designs:
    if check_design(design, towels):
        total += 1

print(total)


with open(r"day 19\towels.txt", "r") as f:
    towels = f.read().split(", ")

with open(r"day 19\designs.txt", "r") as f:
    designs = f.read().split("\n")

max_stripes = 0
for towl in towels:
    max_stripes = max(max_stripes, len(towl))

# -------------------------------------------------------------------

doesnt_work = []
works = {}
def check_permutations_design(design, towels):
    total = 0
    def check_design(design, towels):
        nonlocal total
        total_at_start = total
        if works.get(design) is not None:
            total += works[design]
            return
        if design == "":
            total += 1
            return
        elif design in doesnt_work:
            return
        
        for i in range(max_stripes, -1, -1):
            if design[:i] in towels and i <= len(design):
                check_design(design[i:], towels)
        if total == total_at_start:
            doesnt_work.append(design)
        else:
            works[design] = total - total_at_start
        return
    
    check_design(design, towels)
    return total


total = 0
for design in designs:
    total += check_permutations_design(design, towels)

print(total)

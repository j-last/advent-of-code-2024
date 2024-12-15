
def calc_cost(ax, ay, bx, by, prize_x, prize_y):
    max_b_presses = min(prize_x // bx, prize_y // by) + 1
    for n in range(max_b_presses, -1, -1):
        if (prize_x - (bx*n)) % ax == 0 == (prize_y - (by*n)) % ay:
            if (prize_x - (bx*n)) // ax == (prize_y - (by*n)) // ay:
                return n + 3 * ((prize_x - (bx*n)) // ax)
    return 0

with open(r"day 13\input.txt", "r") as f:
    input = f.read()
    input = input.split("\n")

total_cost = 0
for i in range(0, len(input), 4):
    ax = int(input[i][12:input[i].find(",")])
    ay = int(input[i][input[i].find("Y+")+2:])
    i += 1
    bx = int(input[i][12:input[i].find(",")])
    by = int(input[i][input[i].find("Y+")+2:])
    i += 1
    prize_x = int(input[i][9:input[i].find(",")])
    prize_y = int(input[i][input[i].find("Y=")+2:])

    total_cost += calc_cost(ax, ay, bx, by, prize_x, prize_y)

print(total_cost)

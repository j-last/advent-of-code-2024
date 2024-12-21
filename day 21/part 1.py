codes = ["029A",
"980A",
"179A",
"456A",
"379A"]

numeric_pad = {"A":(2, 3), "0":(1, 3), "1":(0, 2), 
            "2":(1, 2), "3":(2, 2), "4":(0, 1), 
            "5":(1, 1), "6":(2, 1), "7":(0, 0), 
            "8":(1, 0), "9":(2, 0)}

arrow_pad = {"^":(1, 0), "<":(0, 1), "v":(1, 1), ">":(2, 1), "A":(2, 0)}


def get_sequence(code, keypad):
    curr_x, curr_y = keypad["A"]
    sequence = ""
    for digit in code:
        dy = keypad[digit][1] - curr_y
        dx = keypad[digit][0] - curr_x
        if dx > 0 and dy > 0:
            sequence += ">" * dx + "v" * dy
        else:
            if dy > 0:
                sequence += "v" * dy
            else:
                sequence += "^" * abs(dy)
            if dx > 0:
                sequence += ">" * dx
            else:
                sequence += "<" * abs(dx)
        sequence += "A"
        curr_x, curr_y = keypad[digit]
    return sequence


total = 0
for code in codes:
    numeric_part = int(code[:3])
    print(code)
    code = get_sequence(code, numeric_pad)
    print(code)
    code = get_sequence(code, arrow_pad)
    print(code)
    code = get_sequence(code, arrow_pad)
    print(code)
    print()
    total += len(code) * numeric_part
print(total)
        




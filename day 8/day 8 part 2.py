from copy import deepcopy

# Same as part 1 ------------------------------------
def get_all_antenna(input):
    """Returns a dictionary of 
    antenna_symbol : [(x, y) coords of all antenna of that symbol]
    """
    antenna = {}
    for y, row in enumerate(input):
        for x, item in enumerate(row):
            if item != ".":
                if item in antenna:
                    antenna[item].append((x, y))
                else:
                    antenna[item] = [(x, y)]
    return antenna

def antinode_count(input):
    """Creates a list of all antinode locations (x,y) 
    and returns how many of these there are.
    """
    antinode_locations = []

    antennas = get_all_antenna(input)
    for _, antenna_list in antennas.items():
        for i, antenna1 in enumerate(antenna_list):
            for antenna2 in antenna_list[i+1:]:
                for antinode in calc_antinodes(antenna1, antenna2, len(input[0]), len(input[1])):
                    if (0 <= antinode[0] < len(input[0]) and 0 <= antinode[1] < len(input)):
                        antinode_locations.append(antinode)
    # set to remove duplicates (unique antinode locations required)
    return len(set(antinode_locations))
# ----------------------------------------------------

# Part 2 ---------------------------------------------
def calc_antinodes(antenna1, antenna2, max_x, max_y):
    """Takes 2 antenna locations 
    and returns the 2 antinode locations for this pair of antenna
    """
    antinodes = []

    # this will be the starting antenna, which itself is an antinode
    x, y = antenna1
    antinodes.append((x, y))

    dx = antenna1[0] - antenna2[0]
    dy = antenna1[1] - antenna2[1]

    # calculates all antinodes in one direction
    while 0 <= x < max_x and 0 <= y < max_y:
        x -= dx
        y -= dy
        antinodes.append((x, y))

    # and then in the other direction
    x, y = antenna1
    while 0 <= x < max_x and 0 <= y < max_y:
        x += dx
        y += dy
        antinodes.append((x, y))

    return antinodes
# -----------------------------------------------------

# Setup -----------------------------------------------
with open(r"day 8\input.txt", "r") as f:
    input = f.read()
    input = input.split("\n")
    input = [list(row) for row in input]

print(
    antinode_count(input)
)
from copy import deepcopy

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


def calc_antinodes(antenna1, antenna2):
    """Takes 2 antenna locations 
    and returns the 2 antinode locations for this pair of antenna
    """
    dx = antenna1[0] - antenna2[0]
    dy = antenna1[1] - antenna2[1]
    
    antinode1 = (antenna1[0] + dx, antenna1[1] + dy)
    antinode2 = (antenna2[0] - dx, antenna2[1] - dy)

    return (antinode1, antinode2)


def antinode_count(input):
    """Creates a list of all antinode locations (x,y) 
    and returns how many of these there are.
    """
    antinode_locations = []

    antennas = get_all_antenna(input)
    for _, antenna_list in antennas.items():
        for i, antenna1 in enumerate(antenna_list):
            for antenna2 in antenna_list[i+1:]:
                for antinode in calc_antinodes(antenna1, antenna2):
                    if (0 <= antinode[0] < len(input[0]) and 0 <= antinode[1] < len(input)):
                        antinode_locations.append(antinode)
    # set to remove duplicates (unique antinode locations required)
    return len(set(antinode_locations))
                    

with open(r"day 8\input.txt", "r") as f:
    input = f.read()
    input = input.split("\n")
    input = [list(row) for row in input]

print(
    antinode_count(input)
)

GRID_WIDTH = 101
GRID_HEIGHT = 103
SECONDS = 100
with open(r"day 14\input.txt", "r") as f:
    input = f.read()
    input = input.split("\n")


def get_data(file_line):
    """Gets the data from the line of the file in a usable form.
    """
    pos, vel = file_line.split(" ")
    x, y = pos.split(",")
    xvel, yvel = vel.split(",")
    return int(x[2:]), int(y), int(xvel[2:]), int(yvel)

def move(x, y, xvel, yvel, grid_width, grid_height, seconds):
    """Performs a robot's movements, given all the parameters required.
    """
    x += xvel * seconds
    y += yvel * seconds
    x %= grid_width
    y %= grid_height
    return x, y

def get_quadrant(x, y, grid_width, grid_height):
    """Calculates which quadrant a robot is in given an (x,y) coord.
    """
    if y < grid_height // 2:  # top of grid (NORTH)
        if x < grid_width // 2:  # left of grid (WEST)
            return "nw"
        elif x > grid_width // 2:  # right of grid (EAST)
            return "ne"
    elif y > grid_height // 2:  # bottom of grid (SOUTH)
        if x < grid_width // 2:  # left of grid (WEST)
            return "sw"
        elif x > grid_width // 2:  # right of grid (EAST)
            return "se"


quadrants = {"nw": 0, "ne": 0, "sw": 0, "se": 0}

for line in input:
    x, y, xvel, yvel = get_data(line)
    x, y = move(x, y, xvel, yvel, GRID_WIDTH, GRID_HEIGHT, SECONDS)
    quadrant = get_quadrant(x, y, GRID_WIDTH, GRID_HEIGHT)
    if quadrant is not None:
        quadrants[quadrant] += 1


safety_factor = 1
for num_robots in quadrants.values():
    safety_factor *= num_robots

print(safety_factor)

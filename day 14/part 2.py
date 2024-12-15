
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

found = False
seconds = 0
while not found:
    seconds += 1
    grid = [[" " for i in range(GRID_WIDTH)] for j in range(GRID_HEIGHT)]
    for line in input:
        x, y, xvel, yvel = get_data(line)
        x, y = move(x, y, xvel, yvel, GRID_WIDTH, GRID_HEIGHT, seconds)

        grid[y][x] = "#"

    # I do have to admit I googled to see what I was looking for
    # After knowing I was basically just looking for lots of robots in a row oon multiple rows,
    # I trialled and errored the parameters
    times = 0
    for row1 in grid:
        strrow = ""
        for item in row1:
            strrow += str(item)
        if "#"*10 in strrow:
            times += 1
            if times == 10:
                for row in grid:
                    for item in row:
                        print(item, end="")
                    print()
                print(seconds)
                found = True
            


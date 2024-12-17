
# INPUT DATA --------------------------------------------------------
with open(r"day 15\input_grid.txt", "r") as f:
    grid = f.read()
    grid = grid.split("\n")
    grid = list(map(list, grid))

with open(r"day 15\input_movements.txt", "r") as f:
    movements = f.read()

# -------------------------------------------------------------------
def make_movement(robot_x, robot_y, grid, move):
    if move == "^":
        for y in range(robot_y, -1, -1):
            if grid[y][robot_x] == "." or grid[y][robot_x] == "#":
                start_y = y + 1
                break
        for y in range(start_y, robot_y + 1):
            if grid[y-1][robot_x] == ".":
                grid[y-1][robot_x] = grid[y][robot_x]
                grid[y][robot_x] = "."

    elif move == ">":
        for x in range(robot_x, len(grid[robot_y])):
            if grid[robot_y][x] == "." or grid[robot_y][x] == "#":
                start_x = x - 1
                break
        for x in range(start_x, robot_x-1, -1):
            if grid[robot_y][x+1] == ".":
                grid[robot_y][x+1] = grid[robot_y][x]
                grid[robot_y][x] = "."

    elif move == "v":
        for y in range(robot_y, len(grid)):
            if grid[y][robot_x] == "." or grid[y][robot_x] == "#":
                start_y = y - 1
                break
        for y in range(start_y, robot_y-1, -1):
            if grid[y+1][robot_x] == ".":
                grid[y+1][robot_x] = grid[y][robot_x]
                grid[y][robot_x] = "."

    elif move == "<":
        for x in range(robot_x, -1, -1):
            if grid[robot_y][x] == "." or grid[robot_y][x] == "#":
                start_x = x + 1
                break
        for x in range(start_x, robot_x+1):
            if grid[robot_y][x-1] == ".":
                grid[robot_y][x-1] = grid[robot_y][x]
                grid[robot_y][x] = "."

    return grid


# Making the movements
for move in movements:
    if move == "\n": continue
    for rownum in range(len(grid)):
        if "@" in grid[rownum]:
            x, y = grid[rownum].index("@"), rownum
    grid = make_movement(x, y, grid, move)


# Getting the numerical answer value
sumGPS = 0
for rownum, row in enumerate(grid):
    for cellnum, cell in enumerate(row):
        if cell == "O":
            sumGPS += 100 * rownum + cellnum

print(sumGPS)

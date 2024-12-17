
# INPUT DATA --------------------------------------------------------
with open(r"day 15\input_grid.txt", "r") as f:
    grid = f.read()
    grid = grid.split("\n")
    grid = list(map(list, grid))

    for rownum, row in enumerate(grid):
        newrow = []
        for item in row:
            if item == "O":
                newrow += ["[", "]"]
            elif item == "@":
                newrow += ["@", "."]
            else:
                newrow += [item, item]
        grid[rownum] = newrow


with open(r"day 15\input_movements.txt", "r") as f:
    movements = f.read()

# -------------------------------------------------------------------
def move_vert(x, y, grid, val):
    if grid[y][x] == ".":
        return True, grid
    if grid[y+val][x] == "#":
        return False, grid

    if grid[y][x] == "[":
        if grid[y+val][x] != "." or grid[y+val][x+1] != ".":
            leftcan, tempgrid = move_vert(x, y+val, grid, val)
            rightcan, tempgrid = move_vert(x+1, y+val, tempgrid, val)
            if leftcan and rightcan:
                grid = tempgrid
        if grid[y+val][x] == "." and grid[y+val][x+1] == ".":
            grid[y+val][x], grid[y+val][x+1] = "[", "]"
            grid[y][x], grid[y][x+1] = ".", "."
            return True, grid
        return False, grid
    elif grid[y][x] == "]":
        if grid[y+val][x-1] != "." or grid[y+val][x] != ".":
            leftcan, tempgrid = move_vert(x-1, y+val, grid, val)
            rightcan, tempgrid = move_vert(x, y+val, tempgrid, val)
            if leftcan and rightcan:
                grid = tempgrid
        if grid[y+val][x-1] == "." and grid[y+val][x] == ".":
            grid[y+val][x-1], grid[y+val][x] = "[", "]"
            grid[y][x-1], grid[y][x] = ".", "."
            return True, grid
        return False, grid
    else:
        move_vert(x, y+val, grid, val)
        if grid[y+val][x] == ".":
            grid[y+val][x] = grid[y][x]
            grid[y][x] = "."
            return True, grid
        return False, grid
        

            
        
from copy import deepcopy 


def make_movement(robot_x, robot_y, grid, move):
    if move == "^":
        moved, tempgrid = move_vert(robot_x, robot_y, deepcopy(grid), -1)
        if moved:
            grid = tempgrid

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
        moved, tempgrid = move_vert(robot_x, robot_y, deepcopy(grid), 1)
        if moved:
            grid = tempgrid

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
        if cell == "[":
            sumGPS += 100 * rownum + cellnum

print(sumGPS)

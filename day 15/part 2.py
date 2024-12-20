
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
def move_vert_wrapper(x, y, grid, val):
    def move_vert(x, y, val):
        try:
            nonlocal grid

            if grid[y+val][x] == ".":
                grid[y+val][x] = grid[y][x]
                grid[y][x] = "."
            
            else:
                if grid[y+val][x] == "[":
                    move_vert(x, y+val, val)
                    move_vert(x+1, y+val, val)
                elif grid[y+val][x] == "]":
                    move_vert(x, y+val, val)
                    move_vert(x-1, y+val, val)

            if grid[y+val][x] == ".":
                grid[y+val][x] = grid[y][x]
                grid[y][x] = "."
        except IndexError:
            return False
        
    if move_vert(x, y, val) == False:
        return False, grid

    for rownum, row in enumerate(grid):
        for colnum, item in enumerate(row):
            if item == "[" and grid[rownum][colnum+1] != "]":
                return False, grid
    return True, grid
            


    
        

            
        
from copy import deepcopy 


def make_movement(robot_x, robot_y, grid, move):
    if move == "^":
        moved, newgrid = move_vert_wrapper(robot_x, robot_y, deepcopy(grid), -1)
        if moved:
            grid = newgrid
        

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
        moved, newgrid = move_vert_wrapper(robot_x, robot_y, deepcopy(grid), 1)
        if moved:
            grid = newgrid
        

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

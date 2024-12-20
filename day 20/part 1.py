
with open(r"day 20\input.txt", "r") as f:
    input_map = f.read().split("\n")
    grid = []
    for y, row in enumerate(input_map):
        grid.append(list(row))
        if row.find("S") != -1: start = (row.find("S"), y)
        if row.find("E") != -1: end = (row.find("E"), y)

# -------------------------------------------------------------------

def number_path(grid, start, end):
    current = start
    index = 0
    visited = []
    while current != end:
        visited.append(current)
        x, y = current
        grid[y][x] = index
        if grid[y-1][x] != "#" and (x, y-1) not in visited:
            current = (x, y-1)
        elif grid[y][x+1] != "#" and (x+1, y) not in visited:
            current = (x+1, y)
        elif grid[y+1][x] != "#" and (x, y+1) not in visited:
            current = (x, y+1)
        elif grid[y][x-1] != "#" and (x-1, y) not in visited:
            current = (x-1, y)
        index += 1
    x, y = current
    grid[y][x] = index
    return grid


def find_shortcuts(grid):
    total = 0
    for y, row in enumerate(grid):
        for x, num in enumerate(row):
            if num == "#":
                continue

            if y-2 >=0 and grid[y-2][x] != "#" and grid[y-2][x] - num > 100:
                total += 1
            if x+2 < len(grid[0]) and grid[y][x+2] != "#" and grid[y][x+2] - num > 100:
                total += 1
            if y+2 < len(grid) and grid[y+2][x] != "#" and grid[y+2][x] - num > 100:
                total += 1
            if x-2 >= 0 and grid[y][x-2] != "#" and grid[y][x-2] - num > 100:
                total += 1
    return total


grid = number_path(grid, start, end)
print(find_shortcuts(grid))

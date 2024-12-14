
visited = []

def traverse_region(grid, x, y):
    area = 1
    perimeter = 0
    def traverse_cell(x, y):
        nonlocal area
        nonlocal perimeter
        visited.append((x, y))

        # Checks cell to the left
        if x-1 < 0 or grid[y][x-1] != grid[y][x]:  # edge of region
            perimeter += 1
        elif (x-1, y) not in visited:  # region continues to the left
            area += 1
            traverse_cell(x-1, y)
        
        # Checks cell to the right
        if x+1 >= len(grid[0]) or grid[y][x+1] != grid[y][x]:  # edge of region
            perimeter += 1
        elif (x+1, y) not in visited:  # region continues to the right
            area += 1
            traverse_cell(x+1, y)

        # Checks cell above
        if y-1 < 0 or grid[y-1][x] != grid[y][x]:  # edge of region
            perimeter += 1
        elif (x, y-1) not in visited:  # region continues above
            area += 1
            traverse_cell(x, y-1)
        
        # Checks cell below
        if y+1 >= len(grid) or grid[y+1][x] != grid[y][x]:  # edge of region
            perimeter += 1
        elif (x, y+1) not in visited:  # region continues below
            area += 1
            traverse_cell(x, y+1)

    traverse_cell(x, y)
    return area, perimeter


def calculate_cost(grid):
    cost = 0
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if (x, y) not in visited:
                area, perimeter = traverse_region(grid, x, y)
                cost += area * perimeter
    return cost


with open(r"day 12\input.txt", "r") as f:
    input = f.read()
    input = input.split("\n")
    input = list(map(list, input))

print(
    calculate_cost(input)
)

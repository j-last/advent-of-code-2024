from copy import deepcopy

visited = []

def traverse_region(grid, x, y):
    area = 1
    perimeter = 0
    left_sides, right_sides, top_sides, bottom_sides = [], [], [], []
    def traverse_cell(x, y):
        nonlocal area
        nonlocal perimeter
        visited.append((x, y))

        # Checks cell to the left
        if x-1 < 0 or grid[y][x-1] != grid[y][x]:  # edge of region
            perimeter += 1
            left_sides.append((x-1, y))
        elif (x-1, y) not in visited:  # region continues to the left
            area += 1
            traverse_cell(x-1, y)
        
        # Checks cell to the right
        if x+1 >= len(grid[0]) or grid[y][x+1] != grid[y][x]:  # edge of region
            perimeter += 1
            right_sides.append((x+1, y))
        elif (x+1, y) not in visited:  # region continues to the right
            area += 1
            traverse_cell(x+1, y)

        # Checks cell above
        if y-1 < 0 or grid[y-1][x] != grid[y][x]:  # edge of region
            perimeter += 1
            top_sides.append((x, y-1))
        elif (x, y-1) not in visited:  # region continues above
            area += 1
            traverse_cell(x, y-1)
        
        # Checks cell below
        if y+1 >= len(grid) or grid[y+1][x] != grid[y][x]:  # edge of region
            perimeter += 1
            bottom_sides.append((x, y+1))
        elif (x, y+1) not in visited:  # region continues below
            area += 1
            traverse_cell(x, y+1)

    traverse_cell(x, y)
    # After traversing the region, the side data is cleaned up and the total number of sides is calculated
    sides = list(map(clean_up_sides, [left_sides, right_sides, top_sides, bottom_sides]))
    num_sides = 0
    for side_type in sides:
        num_sides += len(side_type)
    return area, num_sides

def clean_up_sides(sides):
    """Takes a list of length 1 sides as input and returns the same list of sides,
    minus the sides that continue on from each other (1-length sides part of the same larger side).
    """
    new_sides = deepcopy(sides)
    for x, y in sides:
        if (x, y+1) in new_sides:
            new_sides.remove((x, y+1))
        if (x+1, y) in new_sides:
            new_sides.remove((x+1, y))
    return new_sides


def calculate_cost(grid):
    cost = 0
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if (x, y) not in visited:
                area, sides = traverse_region(grid, x, y)
                cost += area * sides
    return cost


with open(r"day 12\input.txt", "r") as f:
    input = f.read()
    input = input.split("\n")
    input = list(map(list, input))

print(
    calculate_cost(input)
)

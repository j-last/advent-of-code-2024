

def trailhead_score(grid, y, x):
    def next_step(y, x):
        nonlocal score
        # checks if the current location is an unvisited 9
        if grid[y][x] == 9:
            if (x, y) not in visited_nines:
                score += 1
                visited_nines.append((x, y))
                return
            else:
                return
        # If not it checks right, left, below & above locations for 
        # a location that is 1 higher than it.
        # If at any point one is found, this location is visited (DFS)
        if x+1 < len(grid[y]) and grid[y][x+1] == grid[y][x] + 1:
            next_step(y, x+1)
        if x-1 >= 0 and grid[y][x-1] == grid[y][x] + 1:
            next_step(y, x-1)
        if y+1 < len(grid) and grid[y+1][x] == grid[y][x] + 1:
            next_step(y+1, x)
        if y-1 >= 0 and grid[y-1][x] == grid[y][x] + 1:
            next_step(y-1, x)

    score = 0
    visited_nines = []
    next_step(y, x)
    return score
        

def sum_trail_scores(grid):
    total = 0
    for row_index, row in enumerate(grid):
        for cell_index, height in enumerate(row):
            if row[cell_index] == 0:
                total += trailhead_score(grid, row_index, cell_index)
    return total


with open(r"day 10\input.txt", "r") as f:
    input = f.read()
    input = input.split("\n")
    for i in range(len(input)):
        input[i] = list(map(int, list(input[i])))


print(
    sum_trail_scores(input)
)

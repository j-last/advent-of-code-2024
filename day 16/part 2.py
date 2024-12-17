from math import inf

# INPUT DATA --------------------------------------------------------
with open(r"day 16\input.txt", "r") as f:
    grid = f.read()
    grid = grid.split("\n")
    for rownum, row in enumerate(grid):
        for itemnum, item in enumerate(row):
            if item == "S":
                start = (itemnum, rownum)
            elif item == "E":
                end = (itemnum, rownum)
    
# -------------------------------------------------------------------

def wrapper(start, end):
    path = []
    def dfs(start, end, facing, weight, prev):
        nonlocal path
        if weight > 123540:
            return False
        if start == end:
            return True
        x, y = start
        pathlen = len(path)
        if grid[y-1][x] != "#" and (x, y-1) != prev:
            if facing == "N": 
                if dfs((x, y-1), end, "N", weight + 1, start):
                    path.append((x, y))
            elif dfs((x, y-1), end, "N", weight + 1001, start):
                path.append((x, y))

        if grid[y][x+1] != "#" and (x+1, y) != prev:
            if facing == "E": 
                if dfs((x+1, y), end, "E", weight + 1, start):
                    path.append((x, y))
            elif dfs((x+1, y), end, "E", weight + 1001, start):
                path.append((x, y))
        
        if grid[y+1][x] != "#" and (x, y+1) != prev:
            if facing == "S": 
                if dfs((x, y+1), end, "S", weight + 1, start):
                    path.append((x, y))
            elif dfs((x, y+1), end, "S", weight + 1001, start):
                path.append((x, y))
        
        if grid[y][x-1] != "#" and (x-1, y) != prev:
            if facing == "W": 
                if dfs((x-1, y), end, "W", weight + 1, start):
                    path.append((x, y))
            elif dfs((x-1, y), end, "W", weight + 1001, start):
                path.append((x, y))
        
        if len(path) != pathlen:
            return True
    
    dfs(start, end, "E", 0, None)
    return len(list(set(path))) + 1


print(wrapper(start, end))

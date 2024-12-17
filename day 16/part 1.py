from math import inf

# INPUT DATA --------------------------------------------------------
with open(r"day 16\input.txt", "r") as f:
    grid = f.read()
    grid = grid.split("\n")
    for rownum, row in enumerate(grid):
        for itemnum, item in enumerate(row):
            if item == "S":
                start = (itemnum, rownum, "E")
            elif item == "E":
                end = (itemnum, rownum)
# -------------------------------------------------------------------

def dijkstras(start, end):
    shortest = {start[:-1]: 0}
    queue = [start]
    turns = 0
    while queue:
        # gets the node with the shortest weight to it from the queue
        x, y = None, None
        shortest_weight = inf
        for item in queue:
            xtemp, ytemp, facingtemp = item
            if shortest[(xtemp, ytemp)] < shortest_weight:
                x, y, facing = xtemp, ytemp, facingtemp
                shortest_weight = shortest[(xtemp, ytemp)]
        queue.remove((x, y, facing))
        
        # if the end node is the current node, dijkstras can terminate
        if (x, y) == end:
            return shortest[end]
        
        # explores node above, right, below & left of the current node
        if grid[y-1][x] != "#": 
            weight = 1001
            if facing == "N": weight = 1

            if shortest.get((x, y-1)) is None:
                shortest[(x, y-1)] = shortest[(x, y)]+weight
                queue.append((x, y-1, "N"))
            else: shortest[(x, y-1)] = min(shortest[(x, y-1)], shortest[(x, y)]+weight)

        if grid[y][x+1] != "#": 
            weight = 1001
            if facing == "E": weight = 1
            if shortest.get((x+1, y)) is None:
                shortest[(x+1, y)] = shortest[(x, y)]+weight
                queue.append((x+1, y, "E"))
            else: shortest[(x+1, y)] = min(shortest[(x+1, y)], shortest[(x, y)]+weight)
                
        if grid[y+1][x] != "#": 
            weight = 1001
            if facing == "S": weight = 1
            if shortest.get((x, y+1)) is None:
                shortest[(x, y+1)] = shortest[(x, y)]+weight
                queue.append((x, y+1, "S"))
            else: shortest[(x, y+1)] = min(shortest[(x, y+1)], shortest[(x, y)]+weight)

        if grid[y][x-1] != "#": 
            weight = 1001
            if facing == "W": weight = 1
            if shortest.get((x-1, y)) is None:
                shortest[(x-1, y)] = shortest[(x, y)]+weight
                queue.append((x-1, y, "W"))
            else: shortest[(x-1, y)] = min(shortest[(x-1, y)], shortest[(x, y)]+weight)


print(dijkstras(start, end))

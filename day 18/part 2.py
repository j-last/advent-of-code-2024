from math import inf
GRID_SIZE = 71

grid = [["." for x in range(GRID_SIZE)] for y in range(GRID_SIZE)]
with open(r"day 18\input.txt", "r") as f:
    corrupted_bytes = f.readlines()


def apply_corruptions(corruptions):
    for corruption in corruptions:
        x, y = list(map(int, corruption.split(",")))
        grid[y][x] = "#"
    return grid


def dijkstras(start, end):
    shortest = {start: 0}
    queue = [start]
    while queue:
        # gets the node with the shortest 1 to it from the queue
        # (a lazy implementation of a priority queue)
        x, y = None, None
        shortest_weight = inf
        for item in queue:
            xtemp, ytemp = item
            if shortest[(xtemp, ytemp)] < shortest_weight:
                x, y, = xtemp, ytemp
                shortest_weight = shortest[(xtemp, ytemp)]
        queue.remove((x, y))
        
        # if the end node is the current node, dijkstras can terminate
        if (x, y) == end:
            return shortest[end]
        
        # explores node above, right, below & left of the current square
        if y-1 >=0 and grid[y-1][x] != "#": 
            if shortest.get((x, y-1)) is None:
                shortest[(x, y-1)] = shortest[(x, y)]+1
                queue.append((x, y-1))
            else: shortest[(x, y-1)] = min(shortest[(x, y-1)], shortest[(x, y)]+1)

        if x+1 < len(grid[0]) and grid[y][x+1] != "#":
            if shortest.get((x+1, y)) is None:
                shortest[(x+1, y)] = shortest[(x, y)]+1
                queue.append((x+1, y))
            else: shortest[(x+1, y)] = min(shortest[(x+1, y)], shortest[(x, y)]+1)
                
        if y+1 < len(grid) and grid[y+1][x] != "#":
            if shortest.get((x, y+1)) is None:
                shortest[(x, y+1)] = shortest[(x, y)]+1
                queue.append((x, y+1))
            else: shortest[(x, y+1)] = min(shortest[(x, y+1)], shortest[(x, y)]+1)

        if x-1 >= 0 and grid[y][x-1] != "#": 
            if shortest.get((x-1, y)) is None:
                shortest[(x-1, y)] = shortest[(x, y)]+1
                queue.append((x-1, y))
            else: shortest[(x-1, y)] = min(shortest[(x-1, y)], shortest[(x, y)]+1)
    return False


# from previous task we already know up to 1024 bytes is safe
grid = apply_corruptions(corrupted_bytes[:1024])
for num_bytes in range(1025, len(corrupted_bytes)):
    grid = apply_corruptions([corrupted_bytes[num_bytes]])
    if not dijkstras((0, 0), (GRID_SIZE-1, GRID_SIZE-1)):
        print(corrupted_bytes[num_bytes])
        break

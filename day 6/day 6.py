from time import sleep

def move_vertical(index, direction):
    """diection = 1 for up or -1 for down.
    """
    return index - (ROOM_SIZE * direction)

def move_horizontal(index, direction):
    """direction = 1 for right or -1 for left.
    """
    return index + direction

def traverse_map(lab_map, index):
    direction = 1
    while True:
        while 0 <= move_vertical(index, direction) < len(lab_map) and lab_map[move_vertical(index, direction)] != "#":
            lab_map[index] = "X"
            index = move_vertical(index, direction)
        
        while lab_map[move_horizontal(index, direction)] != "#" and lab_map[move_horizontal(index, direction)] != "\n":
            lab_map[index] = "X"
            index = move_horizontal(index, direction)
        
        if index < 0 or index >= len(lab_map)-(ROOM_SIZE-2) or lab_map[move_horizontal(index, direction)] == "\n":
            break
        direction *= -1

    lab_map[index] = "X"
    return lab_map.count("X")


with open(r"day 6\input_map.txt", "r") as f:
    lab_map = f.read()

ROOM_SIZE = lab_map.find("\n") + 1
guard_startpos = lab_map.find("^")
lab_map = list(lab_map)

distinct_locations = traverse_map(lab_map, guard_startpos)

print(distinct_locations)

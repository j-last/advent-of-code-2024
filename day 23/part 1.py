with open(r"day 23\input.txt", "r") as f:
    connected_computers = f.read().split("\n")

# creates a adjacency list for the connected computers
connections = {}
for connection in connected_computers:
    comp1, comp2 = connection.split("-")
    if connections.get(comp1) is None:
        connections[comp1] = [comp2]
    else:
        connections[comp1].append(comp2)
    if connections.get(comp2) is None:
        connections[comp2] = [comp1]
    else:
        connections[comp2].append(comp1)

# checks through all computer trio combinations and 
# adds them to a list if any of the computers start with a t
trio_found = []
for key, values in connections.items():
    for comp1 in values:
        for comp2 in values:
            if comp1 == comp2:
                continue
            if ({key, comp1, comp2} not in trio_found 
                    and (key[0] == "t" or comp1[0] == "t" or comp2[0] == "t")
                    and key in connections[comp1] 
                    and key in connections[comp2]
                    and comp1 in connections[comp2]):
                trio_found.append({key, comp1, comp2})

# the length of the list is the puzzle answer
print(len(trio_found))

with open(r"day 23\input.txt", "r") as f:
    connected_computers = f.read().split("\n")
    connected_computers = """kh-tc
qp-kh
de-cg
ka-co
yn-aq
qp-ub
cg-tb
vc-aq
tb-ka
wh-tc
yn-cg
kh-ub
ta-co
de-co
tc-td
tb-wq
wh-td
ta-ka
td-qp
aq-cg
wq-ub
ub-vc
de-ta
wq-aq
wq-vc
wh-yn
ka-de
kh-ta
co-tc
wh-qp
tb-vc
td-yn""".split("\n")

# creates a adjacency list for the connected computers
all_comps = []
connections = {}
for connection in connected_computers:
    comp1, comp2 = connection.split("-")
    if comp1 not in all_comps:
        all_comps.append(comp1)
    if comp2 not in all_comps:
        all_comps.append(comp2)
    if connections.get(comp1) is None:
        connections[comp1] = [comp2]
    else:
        connections[comp1].append(comp2)
    if connections.get(comp2) is None:
        connections[comp2] = [comp1]
    else:
        connections[comp2].append(comp1)

max_clique = 0
max_clique_nodes = []
for key, value in connections.items():
    if key[0] != "t":
        continue
    for num in range(1, 2**(len(value))):
        binary = str(bin(num))[2:]
        binary = "0" * (len(value)-len(binary)) + binary
        clique_nodes = set(value)
        for index in range(len(binary)):
            nodes_to_remove = set()
            if binary[index] == "1":
                for item in clique_nodes:
                    if item not in connections[value[index]]:
                        nodes_to_remove |= {item}
                clique_nodes -= nodes_to_remove
            
            if clique_nodes != set(value) and len(clique_nodes) > max_clique:
                print(clique_nodes)
                max_clique = len(clique_nodes)
                max_clique_nodes = clique_nodes


print(max_clique_nodes)







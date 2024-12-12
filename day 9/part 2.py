
def expand_disc(dense_format):
    expanded_format = [0 for i in range(int(input[0]))]
    for i in range(1, len(input), 2):
        for j in range(int(input[i])):
            expanded_format.append(".")
        for j in range(int(input[i+1])):
            expanded_format.append(i//2+1)
    
    return expanded_format


def compact_files(disc):
    spaces = [int(space) for space in disc[1::2]]
    files = [int(file) for file in disc[::2]]
    expanded_disc = expand_disc(disc)
    index = 0
    for i, space in enumerate(spaces):
        index += files[i]
        spaces[i] = [spaces[i], index]
        index += spaces[i][0]
    
    while files:
        for i in range(len(spaces)):
            spacelen = spaces[i][0]
            space_index = spaces[i][1]
            if files[-1] <= spacelen and expanded_disc.index(len(files)-1) > space_index:
                expanded_disc[expanded_disc.index(len(files)-1):expanded_disc.index(len(files)-1)+files[-1]] = ["."] * files[-1]
                expanded_disc[space_index:space_index+files[-1]] = [len(files)-1] * files[-1]
            
                spaces[i][0] -= files[-1]
                spaces[i][1] += files[-1]
                if spaces[i][0] == 0:
                    del spaces[i]
                break
        files = files[:-1]

    return expanded_disc


def calculate_checksum(disc):
    checksum = 0
    for index, filenum in enumerate(disc):
        if filenum != ".":
            checksum += index * filenum
    return checksum


with open(r"day 9\input.txt", "r") as f:
    input = f.read()

compacted_disc = compact_files(input)
checksum_value = calculate_checksum(compacted_disc)

print(checksum_value)
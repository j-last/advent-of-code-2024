
def expand_disc(dense_format):
    expanded_format = [0 for i in range(int(input[0]))]
    for i in range(1, len(input), 2):
        for j in range(int(input[i])):
            expanded_format.append(".")
        for j in range(int(input[i+1])):
            expanded_format.append(i//2+1)
    
    return expanded_format


def compact_files(disc):
    disc = expand_disc(disc)
    while "." in disc:
        next_space = disc.index(".")
        disc[next_space] = disc[-1]
        del disc[-1]
    return disc


def calculate_checksum(disc):
    checksum = 0
    for index, filenum in enumerate(disc):
        checksum += index * filenum
    return checksum


with open(r"day 9\input.txt", "r") as f:
    input = f.read()

compacted_disc = compact_files(input)
checksum_value = calculate_checksum(compacted_disc)

print(checksum_value)

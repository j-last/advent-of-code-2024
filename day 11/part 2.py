
def calc_stones(stones, blinks):
    for i in range(blinks):
        next_step = []
        for stone in stones:
            if stone == 0:
                next_step.append(1)
            elif len(str(stone)) % 2 == 0:
                next_step.append(int(str(stone)[:len(str(stone))//2]))
                next_step.append(int(str(stone)[len(str(stone))//2:]))
            else:
                next_step.append(stone * 2024)
        stones = next_step
        print(i)
    return len(stones)


input = "3 386358 86195 85 1267 3752457 0 741".split(" ")
input = list(map(int, input))

num_stones = calc_stones(input, 75)
print(num_stones)

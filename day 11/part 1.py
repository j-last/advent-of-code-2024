
def calc_stones(stones, blinks):
    num = len(stones)
    def count_stones(stone, blinks_left):
        nonlocal num
        if blinks_left == 0:
            return
        if stone == 0:
            count_stones(1, blinks_left-1)
        elif len(str(stone)) % 2 == 0:
            num += 1
            first_half = int(str(stone)[:len(str(stone))//2])
            second_half = int(str(stone)[len(str(stone))//2:])
            count_stones(first_half, blinks_left-1)
            count_stones(second_half, blinks_left-1)
        else:
            count_stones(stone * 2024, blinks_left-1)
        return
    for stone in stones:
        count_stones(stone, blinks)
    return num


input = "3 386358 86195 85 1267 3752457 0 741".split(" ")
input = list(map(int, input))

num_stones = calc_stones(input, 25)
print(num_stones)

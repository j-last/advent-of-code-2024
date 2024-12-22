
def mix(secret_num, value):
    return secret_num ^ value


def prune(secret_num):
    return secret_num % 16777216


def get_next_num(secret_num):
    secret_num = mix(secret_num, 64 * secret_num)
    secret_num = prune(secret_num)

    secret_num = mix(secret_num, secret_num // 32)
    secret_num = prune(secret_num)

    secret_num = mix(secret_num, 2048 * secret_num)
    secret_num = prune(secret_num)

    return secret_num


with open(r"day 22\input.txt", "r") as f:
    values = f.read().split("\n")
    values = list(map(int, values))

all_prices = []
all_price_changes = []
sequences = []
for valnum, value in enumerate(values):
    prices = [int(str(value)[-1])]
    price_changes = []
    for i in range(2000):
        value = get_next_num(value)
        prices.append(int(str(value)[-1]))
        price_changes.append(prices[-1] - prices[-2])
        if prices[-1] == 9 and price_changes[-4:] not in sequences and len(price_changes[-4:]) == 4:
            sequences.append(price_changes[-4:])
    
    all_prices.append(prices)
    all_price_changes.append(price_changes)

max_total = 0
max_total_index = None

for seq_num, sequence in enumerate(sequences):
    total = 0
    for prices, price_changes in zip(all_prices, all_price_changes):
        for i in range(len(price_changes)-3):
            if [price_changes[i], price_changes[i+1], price_changes[i+2], price_changes[i+3]] == sequence:
                total += prices[i+4]
                break
    if total > max_total:
        max_total = total
        max_total_index = seq_num

print(sequences[max_total_index], max_total)







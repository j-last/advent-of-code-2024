
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

for i in range(2000):
    values = list(map(get_next_num, values))
total = sum(values)
print(total)


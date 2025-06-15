"""
    Doesn't seem very efficient. I don't like this approach.
"""

all_coins = [1, 2, 5, 10, 20, 50, 100, 200]


def sub_thingy(coin, value):
    factor = 1
    while factor * coin <= value:
        yield [coin] * factor, value - factor * coin
        factor += 1


def coin_combinations_of(value, coins=all_coins):
    result = []

    if not coins or coins[0] > value:
        return [[]]

    for i, c in enumerate(coins, 1):
        if c > value:
            break
        for sub_list, sub_value in sub_thingy(c, value):
            for next_list in coin_combinations_of(sub_value, coins[i:]):
                result.append(sub_list + next_list)

    return [x for x in result if x]


if __name__ == "__main__":
    value = 200
    combs = coin_combinations_of(value)
    combs = [c for c in combs if sum(c) == value]
    print(f"Got {len(combs)} combinations")

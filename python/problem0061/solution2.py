from itertools import permutations

top = 150

series = [
    [n * (n + 1) // 2 for n in range(top)],
    [n**2 for n in range(top)],
    [n * (3 * n - 1) // 2 for n in range(top)],
    [n * (2 * n - 1) for n in range(top)],
    [n * (5 * n - 3) // 2 for n in range(top)],
    [n * (3 * n - 2) for n in range(top)],
]


def run():
    for perm in permutations(series):
        for value_list in testing(1000, 10000, perm):
            first, last = value_list[0], value_list[-1]
            if str(last)[-2:] == str(first)[:2]:
                print(f"Resulting sum: {sum(value_list)}")
                return


def testing(start, limit, values):
    for value in filter(lambda v: start < v < limit, values[0]):
        ending = int(str(value)[-2:])
        if ending < 10:
            continue
        if len(values) == 1:
            yield [value]
        else:
            yield from (
                [value, *v]
                for v in testing(ending * 100, (ending + 1) * 100, values[1:])
            )


if __name__ == "__main__":
    run()

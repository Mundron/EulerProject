from itertools import permutations

top = 150

series = {
    "3": [n * (n + 1) // 2 for n in range(top)],
    "4": [n**2 for n in range(top)],
    "5": [n * (3 * n - 1) // 2 for n in range(top)],
    "6": [n * (2 * n - 1) for n in range(top)],
    "7": [n * (5 * n - 3) // 2 for n in range(top)],
    "8": [n * (3 * n - 2) for n in range(top)],
}


def run():
    for index, values in series.items():
        print(f"P_{index} = [{values[0]}, .., {values[-1]}]")
    for perm in permutations(series.items()):
        for value_list in testing(1000, 10000, perm):
            first, last = value_list[0][-1], value_list[-1][-1]
            if str(last)[-2:] == str(first)[:2]:
                print("=" * 50)
                for index, value in value_list:
                    print(f"{index}={value}")
                print(f"Resulting sum: {sum(v[-1] for v in value_list)}")
    print("done")


def testing(start, limit, iterators):
    index, values = iterators[0]
    for position, value in filter(
        lambda v: start < v[-1] < limit, enumerate(values)
    ):
        ending = int(str(value)[-2:])
        if ending < 10:
            continue
        if len(iterators) == 1:
            yield [[f"P_{index},{position}", value]]
        else:
            yield from (
                [[f"P_{index},{position}", value], *v]
                for v in testing(
                    ending * 100, (ending + 1) * 100, iterators[1:]
                )
            )


if __name__ == "__main__":
    run()

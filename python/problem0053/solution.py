def run():
    result, line = 0, [1, 1]
    for n in range(2, 101):
        line = [1, *(sum(line[r : r + 2]) for r in range(n - 1)), 1]
        result += sum(map(lambda v: v > 1e6, line))
    print(f"Endresult: There are {result} values beyond 1,000,000")


def run2():
    line = [1, 1]
    print(
        sum(
            sum(
                map(
                    lambda v: v > 1e6,
                    (
                        line := [
                            1,
                            *(sum(line[r : r + 2]) for r in range(n - 1)),
                            1,
                        ]
                    ),
                )
            )
            for n in range(2, 101)
        )
    )


if __name__ == "__main__":
    run2()

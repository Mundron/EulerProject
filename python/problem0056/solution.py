from itertools import product


def run():
    print(
        max(
            sum(map(int, str(a**b)))
            for a, b in product(range(100), range(100))
        )
    )


if __name__ == "__main__":
    run()

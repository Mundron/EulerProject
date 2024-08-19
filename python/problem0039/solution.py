from collections import Counter


def run(limit):
    solutions = Counter()
    # assume a < b < c
    for p in range(3, limit + 1):
        # p = a + b + c > 3a --> a < p/3
        for a in range(1, p // 3):
            # p = a + b + c > 2a + b --> b < p-2a
            for b in range(a + 1, p - 2 * a):
                c = p - a - b
                if a**2 + b**2 == c**2:
                    solutions[p] += 1

    for k, v in solutions.most_common(1):
        print(f"Maximal soltions is {v} for perimeter {k}")


if __name__ == "__main__":
    run(1000)

from eputils.utils import Prime


def find_closest_fraction(d):
    min_a, min_b, min_dist = 3, 5, 1 / 35
    for b in range(d, 7, -1):
        if b % 7 == 0:
            continue
        db = 3 * b
        a = db // 7
        sb = 7 * b
        delta = db - 7 * a
        if (new_dist := delta / sb) < min_dist:
            min_a, min_b, min_dist = a, b, new_dist
        if (new_dist := (7 - delta) / sb) < min_dist:
            min_a, min_b, min_dist = a + 1, b, new_dist

    return min_a, min_b


def get_proper_fraction(a, b):
    prime = Prime()
    for p in prime():
        while a % p == 0 == b % p:
            a //= p
            b //= p
        if p > a:
            break

    return a, b


def run(d=1_000_000):
    a, b = find_closest_fraction(d)
    a, b = get_proper_fraction(a, b)

    print(f"Result: proper reduced fraction {a} / {b} is closed to 3/7")


if __name__ == "__main__":
    run()

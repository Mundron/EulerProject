from itertools import combinations_with_replacement, combinations
from functools import reduce
from operator import mul

known_primes = [2, 3]


def primes():
    yield from known_primes

    x = known_primes[-1] + 2
    while True:
        for prim in known_primes:
            if not x % prim:
                break
        else:
            yield x
            known_primes.append(x)
        x += 2


def d(number):
    prime_factors = []
    for prim in primes():
        while not number % prim:
            prime_factors.append(prim)
            number //= prim
        if number == 1:
            break

    if len(prime_factors) == 1:
        return 1

    proper_factors = set(prime_factors)

    for l in range(len(prime_factors)):
        for subset in combinations(prime_factors, l):
            proper_factors.add(reduce(mul, subset, 1))

    return sum(proper_factors)


def run(limit):
    abund = []
    for x in range(1, limit + 1):
        if (y := d(x)) > x:
            abund.append(x)

    print(f"Found {len(abund):,} abundant numbers")
    positive_set = set()
    for x, y in combinations_with_replacement(abund, 2):
        positive_set.add(x + y)

    print(f"Result: {sum(set(range(limit)) - positive_set)}")


if __name__ == "__main__":
    run(28123)

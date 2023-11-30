from itertools import combinations
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
    factors = []
    for prim in primes():
        while not number % prim:
            factors.append(prim)
            number //= prim
        if number == 1:
            break

    real_factors = set(factors)
    if len(real_factors) == 1:
        return 1

    for l in range(len(factors)):
        for subset in combinations(factors, l):
            real_factors.add(reduce(mul, subset, 1))

    return sum(real_factors)


def run(limit):
    result = 0
    for x in range(1, limit + 1):
        y = d(x)
        if y < x or y > limit or x == y:
            continue
        if y == x or d(y) == x:
            result += x + y

    print(result)


if __name__ == "__main__":
    run(10000)

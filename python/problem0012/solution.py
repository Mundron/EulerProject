from itertools import count
from functools import reduce
from collections import Counter
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


def factor_cnt(number):
    factors = Counter()
    for prim in primes():
        while not number % prim:
            factors[prim] += 1
            number //= prim
        if number == 1:
            break

    return reduce(mul, map(lambda x: x + 1, factors.values()), 1)


def run(div_limit):
    number = 0
    for x in count(1):
        number += x
        if factor_cnt(number) > div_limit:
            print(number)
            return


if __name__ == "__main__":
    run(500)

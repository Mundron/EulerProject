from eputils.utils import get_primes
from itertools import permutations
from tqdm import tqdm
from math import sqrt

digits = list(map(str, range(1, 10)))


def is_prime(number):
    limit = int(sqrt(number))
    for p in get_primes():
        if number % p == 0:
            return False
        if p > limit:
            break
    return True


def run():
    for length in range(9, 2, -1):
        subdigits = digits[:length]
        print(f"Consider {length}-digit pandigital values")
        size = fact(length)
        results = []
        for perm in tqdm(permutations(subdigits, len(subdigits)), total=size):
            value = int("".join(perm))
            if is_prime(value):
                results.append(value)
        if results:
            print(
                f"Found maximal {length}-digit pandigital prime {max(results)}"
            )
            break


def fact(n):
    if n <= 1:
        return 1
    return n * fact(n - 1)


if __name__ == "__main__":
    run()

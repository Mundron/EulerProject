from eputils.utils import get_prime_factors
from itertools import combinations
from tqdm import tqdm

known_primes = [2, 3, 5, 7, 11]


def prod(args):
    result = 1
    for arg in args:
        result *= arg
    return result


def get_factors(value):
    prime_factors = list(get_prime_factors(value))
    seen_factors = set()
    for length in range(1, len(prime_factors)):
        for fs in map(prod, combinations(prime_factors, length)):
            if fs in seen_factors:
                continue
            yield fs
            seen_factors.add(fs)


def is_pandigit(a, b, c):
    return "".join(sorted(f"{a}{b}{c}")) == "123456789"


def run(limit):
    print(f"Search with upper limit {limit}")
    result = []
    for value in tqdm(range(limit)):
        for fs in get_factors(value):
            rm = value // fs
            if is_pandigit(fs, rm, value):
                result.append([fs, rm, value])
                break
    print(f"Found {len(result):,} results")
    for a, b, c in result:
        print(f"{a} x {b} = {c}")

    print(f"Result is {sum(map(lambda p:p[-1], result))}")


if __name__ == "__main__":
    run(100000)

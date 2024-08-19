from pathlib import Path

prime_path = Path(Path(__file__).parent, "primes.txt")

try:
    with open(prime_path, "r", encoding="utf-8") as fh:
        known_primes = [int(line.strip()) for line in fh]
    print(f"Loaded {len(known_primes):,} known primes")
except FileNotFoundError:
    known_primes = [2, 3, 5, 7, 11]
    with open(prime_path, "w", encoding="utf-8") as fh:
        for p in known_primes:
            fh.write(f"{p}\n")


def get_primes(limit=None):
    if limit:
        for p in known_primes:
            if p > limit:
                break
            yield p
    else:
        yield from known_primes

    p = known_primes[-1] + 1
    while limit is None or p < limit:
        for kp in known_primes:
            if p % kp == 0:
                break
        else:
            yield p
            known_primes.append(p)
            with open(prime_path, "a", encoding="utf-8") as fh:
                fh.write(f"{p}\n")
        p += 1


def prod(args):
    result = 1
    for arg in args:
        result *= arg
    return result


def get_prime_factors(value):
    while value > 1:
        for prime in get_primes():
            if prime > value:
                break
            while value % prime == 0:
                yield prime
                value //= prime


def fact(value):
    if value <= 1:
        return 1
    return value * fact(value - 1)

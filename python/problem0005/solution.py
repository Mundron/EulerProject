from collections import Counter


def factors(value):
    primes = Counter()
    for x in range(2, value + 1):
        while not (value % x):
            primes[x] += 1
            value //= x
        if value == 1:
            break
    return primes


def run(limit):
    primes = Counter()
    for x in range(2, limit + 1):
        subprimes = factors(x)
        for prim, exp in subprimes.items():
            primes[prim] = max(primes[prim], exp)

    result = 1
    for prim, exp in primes.items():
        result *= prim**exp
    print(result)


if __name__ == "__main__":
    run(20)

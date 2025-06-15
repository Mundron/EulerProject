from eputils.utils import Prime


def run(limit=10**6):
    primes = Prime()
    previous_prime = {2: 2, 3: 3}
    prev = 3
    for p in primes(start=5, limit=limit):
        for n in range(prev + 1, p):
            previous_prime[n] = prev
        prev = p
    print(previous_prime)


if __name__ == "__main__":
    run(20)

from math import sqrt
from itertools import count

known_primes = [2, 3]

all_primes = {2, 3}


def primes(limit=None):
    yield from known_primes

    x = known_primes[-1] + 2
    while limit is None or x < limit:
        if x in all_primes:
            known_primes.append(x)
        else:
            for prim in known_primes:
                if not x % prim:
                    break
            else:
                yield x
                known_primes.append(x)
                all_primes.add(x)
        x += 2


def is_prime(number):
    if number < 0:
        return False
    if number in all_primes:
        return True
    for prim in primes(sqrt(number)):
        if number % prim == 0:
            return False
    all_primes.add(number)
    return True


def test_polynom(a, b):
    for n in count():
        if not is_prime(n**2 + a * n + b):
            break

    return n - 1


def run(a_limit, b_limit):
    best_a, best_b, best_con_primes = 0, 0, 0
    for a in range(-a_limit + 1, a_limit):
        for b in primes(b_limit):
            if (con_primes := test_polynom(a, b)) > best_con_primes:
                best_a, best_b, best_con_primes = a, b, con_primes

    print(best_a * best_b)


if __name__ == "__main__":
    run(1000, 1000)

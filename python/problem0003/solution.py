def primes(limit):
    found = []
    for x in range(2, limit):
        for prim in found:
            if not x % prim:
                break
        else:
            yield x
            found.append(x)


def get_max_prime_factor(value):
    for prim in primes(value):
        while not value % prim:
            value //= prim
        if value == 1:
            print(prim)
            break
    else:
        print("No prime factors found")


if __name__ == "__main__":
    get_max_prime_factor(600851475143)

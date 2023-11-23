def primes():
    found, x = [2], 3
    yield 2
    while True:
        for prim in found:
            if not x % prim:
                break
        else:
            yield x
            found.append(x)
        x += 2


def run(position):
    for index, prime in enumerate(primes(), 1):
        if index == position:
            print(prime)
            break


if __name__ == "__main__":
    run(10001)

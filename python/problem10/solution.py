def primes(limit=None):
    found, x = [2], 3
    yield 2
    while limit is None or x < limit:
        for prim in found:
            if not x % prim:
                break
        else:
            yield x
            found.append(x)
        x += 2


print(sum(primes(2 * 10**6)))

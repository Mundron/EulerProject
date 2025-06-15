from eputils.utils import get_primes


def is_strange(n, d, sn, sd):
    if sn[0] == sd[0]:
        return n * int(sd[1]) == d * int(sn[1])
    if sn[0] == sd[1]:
        return n * int(sd[0]) == d * int(sn[1])
    if sn[1] == sd[0]:
        return n * int(sd[1]) == d * int(sn[0])
    if sn[1] == sd[1]:
        return n * int(sd[0]) == d * int(sn[0])
    return False


def run():
    stranges = []
    for n in range(10, 100):
        # force denominator to be greater nominator to have a fraction below 1
        for d in range(n + 1, 100):
            # skip trivial examples
            if not n % 10 and not d % 10:
                continue
            if is_strange(n, d, str(n), str(d)):
                stranges.append((n, d))

    print(f"Found {len(stranges)} strange fractions")
    tn, td = 1, 1
    for n, d in stranges:
        print(f"{n} / {d}")
        tn *= n
        td *= d
    print(f"Got a product {tn} / {td}")
    for p in get_primes():
        if p > min(tn, td):
            break
        while tn % p == 0 and td % p == 0:
            tn //= p
            td //= p
    print(f"In lowest terms {tn} / {td}")


if __name__ == "__main__":
    run()

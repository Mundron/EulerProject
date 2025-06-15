from eputils.utils import Prime
from itertools import permutations


def get_triples(value):
    perms = sorted(
        filter(
            lambda v: v > 1000,
            (int("".join(perm)) for perm in permutations(str(value), 4)),
        )
    )
    for i in range(len(perms) - 2):
        for j in range(i + 1, len(perms) - 1):
            for k in range(j + 1, len(perms)):
                yield perms[i], perms[j], perms[k]


def run():
    prime = Prime()
    known_primes = set()
    known_triples = set()
    for p in prime(10000):
        if p < 1000 or p in known_primes:
            continue
        for a, b, c in get_triples(p):
            # if a in known and b in known and c in known:
            #     continue
            if a == b or b == c:
                continue
            if not (a in prime and b in prime and c in prime):
                continue
            con = f"{a}{b}{c}"
            if con in known_triples:
                continue
            known_primes.update({a, b, c})
            known_triples.add(con)
            if not (c - b == b - a):
                continue
            print(
                f"Found triple {a}, {b}, {c} all primes and "
                f"{c}-{b}={b}-{a}={c-b}"
            )
            print(f"Concatenation: {con}")


if __name__ == "__main__":
    run()

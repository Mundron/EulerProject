from eputils.utils import Prime
from collections import Counter

max_digits = 7

print("Prepare basic masks")
masks = {1 << i: 10**i for i in range(max_digits + 1)}
print(f"Got {len(masks)} basic masks")

for i in range(2 ** (max_digits + 1)):
    orig = i
    parts = []
    for j in range(max_digits, -1, -1):
        pot = 1 << j
        if i >= pot:
            i -= pot
            parts.append(pot)
    if len(parts) > 1:
        masks[orig] = sum(map(masks.get, parts))
print(f"Got {len(masks)} total masks")

nf_shifts = [set(range(-i, 10 - i)) for i in range(10)]
zf_shifts = [set(s) - {-i} for i, s in enumerate(nf_shifts)]


def run(size=8):
    prime = Prime(limit=10**max_digits)
    tested = set()
    for p in prime(start=10, limit=10**max_digits):
        if p in tested:
            continue
        digits = Counter()
        sp = str(p)
        lead = 1 << (len(sp) - 1)
        for i, c in enumerate(reversed(sp)):
            digits[int(c)] |= 1 << i
        for d, r in digits.items():
            shifts = zf_shifts if r >= lead else nf_shifts
            numbers = list(
                filter(
                    lambda n: n in prime, (p + f * masks[r] for f in shifts[d])
                )
            )
            if len(numbers) >= size:
                print(f"Found {size} prime series")
                print(", ".join(map(str, numbers)))
                return


if __name__ == "__main__":
    run(9)

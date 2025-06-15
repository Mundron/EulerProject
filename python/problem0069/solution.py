from eputils.utils import Prime
from itertools import combinations
import json
from tqdm import tqdm

FILE = "divisors.jsonl"
prime = Prime()
facts = {}


def prod(numbers):
    result = 1
    for n in numbers:
        result *= n
    return result


def is_relative_prime(a, i, b, j):
    if i == len(a) or j == len(b):
        return True
    if a[i] < b[j]:
        return is_relative_prime(a, i + 1, b, j)
    elif a[i] > b[j]:
        return is_relative_prime(a, i, b, j + 1)
    # else a[i] == b[j]
    return False


def phi(n):
    if facts[n][0] == n:
        return n - 1

    return (
        sum(is_relative_prime(facts[n], 0, facts[m], 0) for m in range(2, n))
        + 1
    )


def run(limit=10**6):
    if test():
        collect_divisors(limit)
        compute_max_value(limit)


def compute_max_value(limit):
    print(f"Determine maximal n/phi(n) for n=2,..,{limit}")
    max_n, max_val = 2, 2
    # for n in tqdm(range(5, limit + 1), total=limit - 4):
    n = 1
    for p in prime:
        n *= p
        if n > limit:
            break
        if (val := n / phi(n)) > max_val:
            max_n, max_val = n, val

    print(
        f"Result: Max value {max_val:.10f} for n = {max_n}, "
        f"phi({max_n})={phi(max_n)}"
    )


def collect_divisors(limit):
    try:
        print(f"Attempt to load divisors from file {FILE}")
        with open(FILE, "r", encoding="utf-8") as filehandle:
            for key, divisors in map(json.loads, filehandle):
                facts[key] = divisors
        print(f"Loaded {len(facts)} numbers with divisors")
    except FileNotFoundError:
        print(f"File '{FILE}' not found")

    start = max(2, len(facts) + 1)
    if start < limit:
        print(f"Collect factors from {start} until value {limit}")

        for n in tqdm(range(start, limit + 1), total=limit - start + 1):
            facts[n] = list(prime.get_factorization(n).keys())
            if phi(n) <= 0:
                print(f"Error at number {n}")
                print(f"We have divisors {facts[n]}")
                print(f"Numbers below: {n-1}")
                for k in facts[n]:
                    print(f"Remove {n // k} numbers divisible by {k}")
                return

        print(f"Write all {len(facts)} divisors into file")
        with open(FILE, "w", encoding="utf-8") as filehandle:
            for k, v in facts.items():
                filehandle.write(f"{json.dumps([k, v])}\n")


def test():
    expectation = {
        2: 1,
        3: 2,
        4: 2,
        5: 4,
        6: 2,
        7: 6,
        8: 4,
        9: 6,
        10: 4,
        11: 10,
        12: 4,
        13: 12,
        14: 6,
        15: 8,
        16: 8,
        17: 16,
        18: 6,
        19: 18,
        20: 8,
    }
    for n in range(min(expectation.keys()), max(expectation.keys()) + 1):
        facts[n] = list(prime.get_factorization(n).keys())
        if phi(n) != expectation[n]:
            print("=" * 50)
            print("TEST FAILED")
            print(
                f"For n={n} we expected phi({n})={expectation[n]}"
                f" but got {phi(n)}"
            )
            phi(n, verbose=True)
            return False
    print("TEST PASSED")
    return True


if __name__ == "__main__":
    run(10**6)

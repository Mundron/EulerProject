from eputils.utils import get_primes
from tqdm import tqdm

primes = []


def is_truncable_prime(p):
    if p < 10:
        return False
    sp = str(p)
    for i in range(1, len(sp)):
        lt, rt = int(sp[i:]), int(sp[:i])
        if not (lt in primes and rt in primes):
            return False
    return True


def run():
    result = set()
    for p in tqdm(get_primes()):
        primes.append(p)
        if is_truncable_prime(p):
            result.add(p)
            print(f"Found primes {', '.join(map(str, sorted(result)))} ")
        if len(result) == 11:
            break
    print(
        f"Found the seven primes {', '.join(map(str, sorted(result)))} "
        f"with sum {sum(result)}"
    )


if __name__ == "__main__":
    run()

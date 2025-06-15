import yaml
from eputils.utils import get_primes
from tqdm import tqdm


def is_circular(p, primes):
    for position in range(1, len(p)):
        if p[position:] + p[:position] not in primes:
            return False
    return True


def run(limit):
    filename = f"primes_{limit}.yaml"
    try:
        print("Try loading prime numbers")
        with open(filename, "r", encoding="utf-8") as fh:
            primes = yaml.safe_load(fh)
        print(f"Loaded {len(primes):,} prime numbers")
    except FileNotFoundError:
        print(f"Get all primes below {limit}")
        primes = list(map(str, tqdm(get_primes(limit), total=78498)))
        with open(filename, "w", encoding="utf-8") as fh:
            yaml.dump(primes, fh)
        print(f"Saved {len(primes):,} primes into file")

    cp = set()
    for p in tqdm(primes):
        if is_circular(p, primes):
            cp.add(p)

    print(f"Found in total {len(cp)} circular primes")


if __name__ == "__main__":
    run(10**6)

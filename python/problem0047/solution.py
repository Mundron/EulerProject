from itertools import count
from eputils.utils import Prime
from tqdm import tqdm


def run(d):
    prime = Prime()
    for number in tqdm(count()):
        factors = {}
        for i in range(d):
            factors[number + i] = prime.get_factorization(number + i)
            if len(factors[number + i]) != d:
                break
        if (
            len(factors) == d
            and sum(len(f) for f in factors.values()) == d**2
        ):
            print(
                "Found four consecutive integers with four distinct prime "
                "factors each"
            )
            for key, values in factors.items():
                fs = " x ".join(
                    map(lambda kv: f"{kv[0]}^{kv[1]}", values.items())
                )
                print(f"{key}={fs}")
            break


if __name__ == "__main__":
    run(4)

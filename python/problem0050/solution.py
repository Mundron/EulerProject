from eputils.utils import Prime
from tqdm import tqdm


def run(limit=10**6):
    prime = Prime()
    ps, s = [], 0
    for p in prime:
        s += p
        if s > limit:
            break
        ps.append(p)
    print(
        f"Collected {len(ps)} primes which sum up to {s:,} just below "
        f"{limit:,}"
    )
    print(f"Max known prime: {prime.sorted[-1]:,}")

    for length in range(len(ps), -1, -1):
        for start in range(len(ps) - length + 1):
            sequence = ps[start : start + length]
            number = sum(sequence)
            if number in prime:
                print(
                    f"Found prime {number} which is sum of consecutives "
                    f"primes {sequence[0]} + .. + {sequence[-1]} which is "
                    f"{len(sequence)} long."
                )
                return


if __name__ == "__main__":
    run()

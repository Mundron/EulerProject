from eputils.utils import Prime
from itertools import count
from math import sqrt


def run():
    primes = Prime()
    for number in count(3, 2):
        for p in primes:
            if p > number:
                print(f"Found {number} which contradicts conjecture")
                return
            s = number - p
            hs = s // 2
            if s % 2 == 0 and int(sqrt(hs)) ** 2 == hs:
                break


if __name__ == "__main__":
    run()

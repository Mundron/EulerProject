from itertools import count
from eputils.utils import Prime
from time import time


def run():
    prime = Prime()
    start_time = time()
    numbers, primes = 1, 0
    next_number = 1
    for layer in count(2, 2):
        for i in range(1, 5):
            next_number += layer
            primes += prime.is_prime(next_number)
        numbers += 4
        if 10 * primes < numbers:
            print(
                f"At layer {layer//2} with side length {layer+1} we get "
                f"a ratio of {primes}/{numbers}={100*primes / numbers:.1f}%"
            )
            break
    print(f"Runtime: {time()-start_time}")


if __name__ == "__main__":
    run()

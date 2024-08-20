from collections import Counter
from pathlib import Path
from math import inf

prime_path = Path(Path(__file__).parent, "primes.txt")

try:
    with open(prime_path, "r", encoding="utf-8") as fh:
        known_primes = [int(line.strip()) for line in fh]
    print(f"Loaded {len(known_primes):,} known primes")
except FileNotFoundError:
    known_primes = [2, 3, 5, 7, 11]
    with open(prime_path, "w", encoding="utf-8") as fh:
        for p in known_primes:
            fh.write(f"{p}\n")


def get_primes(limit=None):
    if limit:
        for p in known_primes:
            if p > limit:
                break
            yield p
    else:
        yield from known_primes

    p = known_primes[-1] + 1
    while limit is None or p < limit:
        for kp in known_primes:
            if p % kp == 0:
                break
        else:
            yield p
            known_primes.append(p)
            with open(prime_path, "a", encoding="utf-8") as fh:
                fh.write(f"{p}\n")
        p += 1


def prod(args):
    result = 1
    for arg in args:
        result *= arg
    return result


def get_prime_factors(value):
    while value > 1:
        for prime in get_primes():
            if prime > value:
                break
            while value % prime == 0:
                yield prime
                value //= prime


def fact(value):
    if value <= 1:
        return 1
    return value * fact(value - 1)


class Series:
    def __init__(self, index=1, value=1, values=None):
        if values:
            self.sorted = values
            self.known = set(values)
            self.index = len(values)
            self.value = values[-1]
        else:
            self.index, self.value = index, value
            self.known = {value}
            self.sorted = [value]
        self.iter_limit = inf

    def __contains__(self, number):
        while number > self.value:
            self.add_next()

        return number in self.known

    def get(self, index):
        while index + 1 > len(self.sorted):
            self.add_next()
        return self.sorted[index]

    def add_next(self):
        self.known.add(self.value)
        self.sorted.append(self.value)

    def __iter__(self):
        self.current_index = -1
        return self

    def __call__(self, limit):
        self.iter_limit = limit
        return self.__iter__()

    def __next__(self):
        self.current_index += 1
        while self.current_index + 1 > len(self.sorted):
            self.add_next()
        result = self.sorted[self.current_index]
        if result > self.iter_limit:
            self.iter_limit = inf
            raise StopIteration
        return result


class Prime(Series):
    def __init__(self):
        with open(prime_path, "r", encoding="utf-8") as fh:
            values = [int(line.strip()) for line in fh]
        super().__init__(values=values)

    def add_next(self):
        while True:
            self.value += 1
            for kp in self.known:
                if self.value % kp == 0:
                    break
            else:
                break
        with open(prime_path, "a", encoding="utf-8") as fh:
            fh.write(f"{self.value}\n")
        super().add_next()

    def get_factorization(self, number):
        if abs(number) <= 1:
            return {}
        # print(f"Get factorization for {number}")
        result = Counter()
        for p in self:
            # print(f"Check for prime {p}")
            while number % p == 0:
                result[p] += 1
                number //= p
                # print(f"Had divisibility by {p} and remaining {number}")
            if abs(number) == 1:
                return result
            # if p > 10:
            #     break


class Triagonal(Series):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def add_next(self):
        self.index += 1
        self.value = self.index * (self.index + 1) // 2
        super().add_next()


class Pentagonal(Series):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def add_next(self):
        self.index += 1
        self.value = self.index * (3 * self.index - 1) // 2
        super().add_next()


class Hexagonal(Series):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def add_next(self):
        self.index += 1
        self.value = self.index * (2 * self.index - 1)
        super().add_next()

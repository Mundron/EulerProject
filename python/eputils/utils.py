from collections import Counter
from pathlib import Path
from math import inf, sqrt

folder = Path(__file__).parent


def prod(args):
    result = 1
    for arg in args:
        result *= arg
    return result


def fact(value):
    if value <= 1:
        return 1
    return value * fact(value - 1)


class Series:
    def __init__(self, name, value=1, limit=None):
        try:
            self.path = Path(folder, f"{name}.txt")
            with open(self.path, "r", encoding="utf-8") as fh:
                values = []
                for line in fh:
                    value = int(line.strip())
                    if limit and value > limit:
                        break
                    values.append(value)
        except FileNotFoundError:
            values = [value]

        self.sorted = values
        self.known = set(values)
        self.index = len(values)
        self.value = values[-1]

        self.iter_start = 0
        self.iter_limit = inf

        self.limited = limit

    def __contains__(self, number):
        while number > self.value:
            self.add_next()

        return number in self.known

    def get(self, index):
        while index + 1 > len(self.sorted):
            self.add_next()
        return self.sorted[index]

    def add_next(self):
        if self.limited and self.value >= self.limited:
            raise ValueError(
                "Attempt to use series beyond given limitation of "
                f"{self.limited}"
            )
        self.known.add(self.value)
        self.sorted.append(self.value)
        with open(self.path, "a", encoding="utf-8") as fh:
            fh.write(f"{self.value}\n")

    def __iter__(self):
        self.current_index = -1
        return self

    def __call__(self, start=0, limit=inf):
        self.iter_start = start
        self.iter_limit = limit
        return self.__iter__()

    def __next__(self):
        result = self.iter_start - 1
        while result < self.iter_start:
            self.current_index += 1
            while self.current_index + 1 > len(self.sorted):
                self.add_next()
            result = self.sorted[self.current_index]

        if result > self.iter_limit:
            self.iter_start = 0
            self.iter_limit = inf
            raise StopIteration
        return result


class Prime(Series):
    def __init__(self, *args, **kwargs):
        super().__init__("primes", 2, *args, **kwargs)

    def add_next(self):
        while True:
            self.value += 1
            is_prime, svalue = True, sqrt(self.value)
            for kp in self.known:
                if kp > svalue:
                    break
                if self.value % kp == 0:
                    is_prime = False
                    break
            if is_prime:
                break
        super().add_next()

    def get_factorization(self, number):
        if abs(number) <= 1:
            return {}
        result = Counter()
        for p in self:
            while number % p == 0:
                result[p] += 1
                number //= p
            if abs(number) == 1:
                return result


class Triagonal(Series):
    def __init__(self, *args, **kwargs):
        super().__init__("triagonals", 1, *args, **kwargs)

    def add_next(self):
        self.index += 1
        self.value = self.index * (self.index + 1) // 2
        super().add_next()


class Pentagonal(Series):
    def __init__(self, *args, **kwargs):
        super().__init__("pentagonals", 1, *args, **kwargs)

    def add_next(self):
        self.index += 1
        self.value = self.index * (3 * self.index - 1) // 2
        super().add_next()


class Hexagonal(Series):
    def __init__(self, *args, **kwargs):
        super().__init__("hexagonals", 1, *args, **kwargs)

    def add_next(self):
        self.index += 1
        self.value = self.index * (2 * self.index - 1)
        super().add_next()

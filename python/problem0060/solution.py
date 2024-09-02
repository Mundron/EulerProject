from itertools import combinations
from math import sqrt


class PrimeGenerator:
    def __init__(self):
        self.sorted_primes = [2, 3, 5, 7, 11]
        self.iter_start = 0
        self.current_index = -1
        self.index_flip = True

    def __call__(self, start=0):
        self.iter_start = start
        return self.__iter__()

    def __iter__(self):
        self.current_index = -1
        return self

    def __next__(self):
        result = self.iter_start - 1
        while result < self.iter_start:
            self.current_index += 1
            if self.current_index + 1 > len(self.sorted_primes):
                self._add_next()
            result = self.sorted_primes[self.current_index]
        return result

    def _add_next(self):
        next_value = self.sorted_primes[-1]
        while True:
            if self.index_flip:
                next_value += 2
            else:
                next_value += 4
            self.index_flip = not self.index_flip
            is_prime, svalue = True, int(sqrt(next_value))
            for prime in self.sorted_primes:
                if prime > svalue:
                    break
                if next_value % prime == 0:
                    is_prime = False
                    break
            if is_prime:
                break
        self.sorted_primes.append(next_value)


def concat(p1, p2):
    return int(f"{p1}{p2}")


class PrimeTester:
    def __init__(self):
        self.primes = PrimeGenerator()

    def is_prime(self, value):
        svalue = int(sqrt(value))
        for prime in self.primes:
            if prime > svalue:
                break
            if value % prime == 0:
                return False
        return True

    def related_primes(self, p1, p2):
        return self.is_prime(concat(p1, p2)) and self.is_prime(concat(p2, p1))


def run(size=5):
    primes = PrimeGenerator()
    tester = PrimeTester()
    relation = {3: set()}
    for p1 in primes(start=7):
        tmp = set()
        for p2 in relation.keys():
            if tester.related_primes(p1, p2):
                tmp.add(p2)
        relation[p1] = set()
        for p2 in tmp:
            rel = relation[p2]
            if len(rel) < size - 2:
                rel.add(p1)
                continue
            intersection = rel & tmp
            rel.add(p1)
            if len(intersection) < size - 2:
                continue
            for subset in combinations(intersection, size - 2):
                for pair in combinations(subset, 2):
                    if not tester.related_primes(*pair):
                        break
                else:
                    result = {p1, *subset, p2}
                    print(
                        f"Found: {sorted(result)} and the sum is {sum(result)}"
                    )
                    return


if __name__ == "__main__":
    run()

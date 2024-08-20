from itertools import permutations

digits = list(map(str, range(10)))
primes = [2, 3, 5, 7, 11, 13, 17]


def get_pandigital():
    for perm in permutations(digits, len(digits)):
        yield int("".join(perm))


def has_property(number):
    number = str(number)
    for i in range(7):
        if int(number[i + 1 : i + 4]) % primes[i] != 0:
            return False
    return True


def run():
    print(sum(filter(has_property, get_pandigital())))


if __name__ == "__main__":
    run()

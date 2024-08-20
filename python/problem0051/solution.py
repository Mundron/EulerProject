from eputils.utils import Prime
from itertools import permutations

patterns = {}
number_sets = permutations(map(str, range(10)), 8)


def get_pattern(value):
    for count in range(1, len(value) - 1):
        if count not in patterns:
            basis = "d" * (len(value) - count) + "*" * count
            patterns[count] = [
                "".join(perm) for perm in permutations(basis, len(basis))
            ]
        yield from patterns[count]


def get_patterned_number(value):
    value = str(value)
    for pattern in get_patter(value):
        yield "".join(x if x == "*" else y for x, y in zip(pattern, value))


def replaced_numbers(value):
    for patterned in get_patterned_number(value):
        for nset in number_sets:
            for n in nset:
                yield int(patterned.replace("*", n))


def run():
    prime = Prime()


if __name__ == "__main__":
    run()

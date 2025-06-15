from itertools import count
from collections import defaultdict


def run():
    found, length = defaultdict(list), 0
    for number in map(str, map(lambda x: x**3, count())):
        if len(number) > length:
            for key, values in found.items():
                if len(values) == 5:
                    print(values[0])
                    return
            found, length = defaultdict(list), len(number)
        found["".join(sorted(number))].append(number)


if __name__ == "__main__":
    run()

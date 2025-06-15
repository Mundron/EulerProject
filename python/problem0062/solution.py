from itertools import count
from collections import defaultdict


def run():
    found = defaultdict(list)
    length = 0
    for n in count():
        number = str(n**3)
        if len(number) > length:
            for key, values in found.items():
                if len(values) == 5:
                    print(f"Key: {key}")
                    for x in values:
                        print(f"{x}**3 = {x**3}")
                    return
            print(f"No example found for length {length}")
            del found
            found = defaultdict(list)
            length = len(number)
        found["".join(sorted(number))].append(n)


if __name__ == "__main__":
    run()

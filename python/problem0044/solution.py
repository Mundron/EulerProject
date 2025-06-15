from eputils.utils import Pentagonal
from math import inf
from itertools import count
from tqdm import tqdm


def run():
    penta = Pentagonal(True)
    D = inf
    for ti in count(1, 1):
        pt = penta.get(ti)
        if pt - penta.get(ti - 1) > D:
            print(f"Total break since {pt} - {penta.get(ti - 1)} > {D}")
            break
        for bi in range(ti - 1, -1, -1):
            # print(f"Decrease inner index to {bi} with outer index {ti}")
            pb = penta.get(bi)
            diff = pt - pb
            if diff > D:
                break
            if diff in penta and pt + pb in penta:
                print(
                    f"Found a pair P_{ti}={pt} and P_{bi}={pb} with D={diff}"
                )
                D = diff

    print(f"Result: D={diff}")


if __name__ == "__main__":
    run()

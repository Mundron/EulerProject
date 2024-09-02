from pathlib import Path
from itertools import product
import numpy as np


def minimal():
    with open(
        Path(Path(__file__).parent, "cipher.txt"), "r", encoding="utf-8"
    ) as fh:
        encrypted = np.array(list(map(int, fh.read().split(","))))

    repeat = len(encrypted) // 3
    tail = len(encrypted) - 3 * repeat
    for xyz in product(range(ord("a"), ord("z")), repeat=3):
        decrypted = encrypted ^ np.array(xyz * repeat + xyz[:tail])
        if " and " in "".join(map(chr, decrypted)):
            print(decrypted.sum())
            break


if __name__ == "__main__":
    minimal()

from tqdm import tqdm
from math import sqrt, inf, ceil


def get_x(D, verbose=False, limit=0):
    x = ceil(sqrt(D))
    if x**2 == D:
        return -inf
    # if verbose:
    #     print("=" * 50)
    #     print(f"x^2-{D}*y^2 == 1")
    y = 1
    rounds = 0
    sd = sqrt(D)
    # while True:
    while not limit or rounds < limit:
        if (poly := x**2 - D * (y**2)) < 1:
            if verbose:
                print(f" -> {x}^2 - {D} * {y}^2 == {poly} < 1")
            x = ceil(sd * y)
        elif poly > 1:
            if verbose:
                print(f" -> {x}^2 - {D} * {y}^2 == {poly} > 1")
            y = ceil(x / sd)
        else:
            if verbose:
                print(f" -> {x}^2 - {D} * {y}^2 == 1")
            return x
        rounds += 1

    print(f" -> {x}^2 - {D} * {y}^2 == {poly} != 1")
    return -inf


# print(max(tqdm(range(2, 1001)), key=get_x))
get_x(61, True, 10)
# for D in range(2, 8):
# get_x(D, True)

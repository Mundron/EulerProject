from math import sqrt
from tqdm import tqdm
from multiprocessing import Pool

ERROR = 1e-7


def get_period(n):
    value = sqrt(n)
    x = int(value)
    value -= x
    if value == 0:
        # print(f"sqrt({n}) = {x} = [{x}; (0)]")
        return 0
    # sequence = [x]
    remainings = [value]
    # print(f"Consider sqrt({n})")
    while True:
        # for i in range(10):
        x = int(1 / value)
        value = 1 / value - x
        # sequence.append(x)
        # print(f"a_{i+1}={x}, remaining {value:.3f}")
        # print("-" * 50)
        for index, r in enumerate(remainings, start=1):
            if abs(value - r) < ERROR:
                # print(
                #     f"sqrt({n})=["
                #     + "; ".join(map(str, sequence[:index]))
                #     + "; ("
                #     + ", ".join(map(str, sequence[index:]))
                #     + ")]"
                #     + f", period={len(sequence) - index}"
                # )
                # return len(sequence) - index
                return (len(remainings) - index + 1) % 2 == 1
            # else:
            #     print(f"Diff to {index}: {abs(value - r)}")
        remainings.append(value)


def run(batchsize=20, limit=10000):
    result = 0
    for n in tqdm(range(2, limit batchsize)):
        with Pool(batchsize) as p:
            result += sum(
                p.map(get_period, range(n, max(n + batchsize, limit)))
            )
    print(result)


def test(x):
    return x % 2 == 0


if __name__ == "__main__":
    run()
    # get_period(31)
    # with Pool(30) as p:
    #     print(sum(p.map(test, [2, 3, 3, 4, 1, 12, 314, 5123, 13231556])))

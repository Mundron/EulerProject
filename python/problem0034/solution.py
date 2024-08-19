from eputils.utils import fact
from tqdm import tqdm

nf = fact(9)


def is_curious(svalue, value, verbose=False):
    digits = list(map(int, svalue))
    if verbose:
        sd = "+".join(map(lambda d: f"{d}!", digits))
        sf = "+".join(map(str, map(fact, digits)))
        sv = sum(map(fact, digits))
        print(f"We get {sd} = {sf} = {sv} matching {value} is {sv == value}")
        return sv == value
    else:
        return sum(map(fact, digits)) == value


def run():
    length = 2
    numbers = []
    while 10**length < (length + 1) * nf:
        print(f"Check range {10**length} to {10**(length+1)-1}")
        for value in tqdm(range(10**length, 10 ** (length + 1))):
            svalue = str(value)
            if fact(int(max(svalue))) > int(value):
                continue
            if is_curious(svalue, value):
                numbers.append(value)
        print(f"Found {len(numbers)} curious numbers so far.")
        length += 1
    print(f"Its sum is {sum(numbers)}")


if __name__ == "__main__":
    run()

from collections import Counter
from itertools import count


def get_digits(number):
    result = Counter()
    for c in str(number):
        result[c] += 1
    return result


def test_number(number):
    baseline = get_digits(number)
    for f in range(2, 7):
        if get_digits(f * number) != baseline:
            return False
    return True


def run():
    for number in count(1, 1):
        if test_number(number):
            print(f"Found number {number}")
            for f in range(1, 7):
                print(f * number)
            return


if __name__ == "__main__":
    run()

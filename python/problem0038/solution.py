digits = list(map(str, range(1, 10)))


def is_pandigital(number):
    return sorted(number) == digits


def conprod(number):
    result = ""
    for f in range(1, 10):
        result += str(number * f)
        if len(result) > 9:
            return None, None
        elif len(result) == 9:
            return result, f"Concated {number} with {tuple(range(1, f + 1))}"
    return None


def run():
    result = 1
    for i in range(10**5):
        cp, msg = conprod(i)
        if cp is not None and is_pandigital(cp):
            cp = int(cp)
            if result < cp:
                print(f"Next higher pandigital value: {cp}")
                print(msg)
                result = cp
    print(f"Result: {result}")


if __name__ == "__main__":
    run()

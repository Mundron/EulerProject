twos = []


def is_palindrom(number):
    for p in range(len(number) // 2):
        if number[p] != number[len(number) - p - 1]:
            return False
    return True


def binary(number):
    for index in range(len(twos) - 1, -1, -1):
        if number >= twos[index]:
            break

    result = ""
    for i in range(index, -1, -1):
        if number >= twos[i]:
            result += "1"
            number -= twos[i]
        else:
            result += "0"
    return result


def compute_twos(limit):
    print(f"Compute potencies of two until {limit:,}")
    value = 1
    while value < limit:
        twos.append(value)
        value *= 2
    print(f"Got {len(twos):,} values")


def run(limit):
    compute_twos(limit)
    bipalin = []
    for number in range(limit):
        if is_palindrom(str(number)) and is_palindrom(binary(number)):
            bipalin.append(number)
    print("\n".join(map(str, bipalin)))
    print(f"Found {len(bipalin):,} numbers. Its sum is {sum(bipalin)}")


if __name__ == "__main__":
    run(10**6)

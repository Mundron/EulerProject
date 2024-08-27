def inverse(number):
    return int("".join(reversed(str(number))))


def run():
    is_lychrel = {}
    for number in range(10_000):
        next_number, next_inverse = number, inverse(number)
        for i in range(51):
            next_number += next_inverse
            if next_number == (next_inverse := inverse(next_number)):
                is_lychrel[number] = False
                break
        else:
            is_lychrel[number] = True

    print(f"There are {sum(is_lychrel.values())} Lychrel numbers below 10,000")


if __name__ == "__main__":
    run()
